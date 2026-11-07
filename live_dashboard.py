import os
import sys
import time
import json
import threading
from pathlib import Path
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import MetaTrader5 as mt5
import webview

# Load environment variables
load_dotenv()


class DashboardApi:
    """JS-to-Python Bridge API exposed to pywebview window as window.pywebview.api"""
    def __init__(self, dashboard):
        self.db = dashboard

    def emergency_reset(self):
        return self.db.emergency_reset()

    def delete_pendings(self):
        return self.db.delete_pendings()

    def clear_history(self):
        return self.db.clear_history()

    def generate_report(self):
        return self.db.generate_report()


class LivePortfolioDashboard:
    def __init__(self):
        self.running = True
        self.magic_buy = 777001
        self.magic_sell = 777002
        self.magic_ai = 234000
        self.history_days = 30
        
        self.reset_timestamp, self.session_max_drawdown, self.start_balance = self._load_reset_config()
        self.trade_history = []
        self.metrics = {
            'total_trades': 0,
            'win_rate': 0.0,
            'total_pnl': 0.0,
            'profit_factor': 0.0,
            'max_drawdown': 0.0
        }
        self.equity_history = self._load_chart_history()
        self._last_chart_append = 0
        self._log_file_path = None
        self._last_log_pos = 0
        self.window = None

    # -----------------------------------------------------------------------
    # Config & State Persistence
    # -----------------------------------------------------------------------
    def _save_reset_config(self):
        try:
            config_file = Path("logs/reset_config.json")
            config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'reset_timestamp': self.reset_timestamp,
                    'session_max_drawdown': self.session_max_drawdown,
                    'start_balance': self.start_balance
                }, f, indent=2)
        except Exception as e:
            print(f"[Dashboard] Failed to save reset config: {e}")

    def _load_reset_config(self):
        try:
            config_file = Path("logs/reset_config.json")
            if config_file.exists() and config_file.stat().st_size > 0:
                with open(config_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return (
                        data.get('reset_timestamp', 0),
                        data.get('session_max_drawdown', 0.0),
                        data.get('start_balance', 0.0)
                    )
        except Exception:
            pass
        return 0, 0.0, 0.0

    def _load_chart_history(self):
        try:
            path = Path("logs/chart_history.json")
            if path.exists() and path.stat().st_size > 0:
                with open(path, 'r', encoding='utf-8') as f:
                    history = json.load(f)
                    if isinstance(history, list) and len(history) > 0:
                        return history
        except Exception:
            pass
        return [self.start_balance] if self.start_balance > 0 else []

    def _save_chart_history(self):
        try:
            path = Path("logs/chart_history.json")
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(self.equity_history, f)
        except Exception:
            pass

    # -----------------------------------------------------------------------
    # Interactive Actions Triggered from UI Buttons via js_api
    # -----------------------------------------------------------------------
    def delete_pendings(self):
        """Delete all pending orders in MT5"""
        try:
            orders = mt5.orders_get()
            deleted = 0
            if orders:
                for o in orders:
                    res = mt5.order_send({"action": mt5.TRADE_ACTION_REMOVE, "order": o.ticket})
                    if res and res.retcode == mt5.TRADE_RETCODE_DONE:
                        deleted += 1
            return {"status": "ok", "deleted": deleted, "message": f"Deleted {deleted} pending orders."}
        except Exception as e:
            return {"status": "error", "message": f"Delete pendings failed: {e}"}

    def clear_history(self):
        """Reset persistent chart and session metrics without closing active trades"""
        try:
            acc = mt5.account_info()
            self.start_balance = acc.balance if acc else 0.0
            self.reset_timestamp = int(time.time())
            self.session_max_drawdown = 0.0
            self._save_reset_config()

            self.trade_history = []
            self.equity_history = [self.start_balance] if self.start_balance > 0 else []
            self._save_chart_history()
            self.metrics = {
                'total_trades': 0, 'win_rate': 0.0, 'total_pnl': 0.0,
                'profit_factor': 0.0, 'max_drawdown': 0.0
            }
            return {"status": "ok", "message": "Dashboard metrics and chart history cleared."}
        except Exception as e:
            return {"status": "error", "message": f"Clear history failed: {e}"}

    def emergency_reset(self):
        """Close ALL positions, delete pendings, wipe grid state, reset metrics"""
        try:
            positions = mt5.positions_get()
            closed_count = 0
            if positions:
                for p in positions:
                    action = mt5.ORDER_TYPE_SELL if p.type == mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY
                    tick = mt5.symbol_info_tick(p.symbol)
                    if tick:
                        price = tick.bid if p.type == mt5.POSITION_TYPE_BUY else tick.ask
                        request = {
                            "action": mt5.TRADE_ACTION_DEAL,
                            "symbol": p.symbol,
                            "volume": p.volume,
                            "type": action,
                            "position": p.ticket,
                            "price": price,
                            "deviation": 20,
                            "magic": p.magic,
                            "comment": "EMERGENCY_RESET",
                            "type_time": mt5.ORDER_TIME_GTC,
                            "type_filling": mt5.ORDER_FILLING_IOC,
                        }
                        res = mt5.order_send(request)
                        if res and res.retcode == mt5.TRADE_RETCODE_DONE:
                            closed_count += 1

            orders = mt5.orders_get()
            deleted_count = 0
            if orders:
                for o in orders:
                    res = mt5.order_send({"action": mt5.TRADE_ACTION_REMOVE, "order": o.ticket})
                    if res and res.retcode == mt5.TRADE_RETCODE_DONE:
                        deleted_count += 1

            state_file = Path("logs/grid_state.json")
            if state_file.exists():
                try:
                    state_file.unlink()
                except Exception:
                    pass

            acc = mt5.account_info()
            self.start_balance = acc.balance if acc else 0
            self.reset_timestamp = int(time.time())
            self._save_reset_config()
            self.trade_history = []
            self.equity_history = [self.start_balance] if self.start_balance > 0 else []
            self._save_chart_history()

            return {
                "status": "ok",
                "closed": closed_count,
                "deleted": deleted_count,
                "message": f"EMERGENCY RESET: Closed {closed_count} pos, deleted {deleted_count} pendings."
            }
        except Exception as e:
            return {"status": "error", "message": f"Emergency reset failed: {e}"}

    def generate_report(self):
        """Export comprehensive JSON and standalone HTML performance report"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            report_dir = Path("logs/live_reports")
            report_dir.mkdir(parents=True, exist_ok=True)
            
            json_path = report_dir / f"dashboard_report_{timestamp}.json"
            html_path = report_dir / f"performance_report_{timestamp}.html"
            
            profits = [t['profit'] for t in self.trade_history]
            total_loss = sum(abs(p) for p in profits if p < 0)
            total_profit = sum(p for p in profits if p > 0)
            
            report_data = {
                'timestamp': datetime.now().isoformat(),
                'metrics': {
                    **self.metrics,
                    'total_loss': total_loss,
                    'total_gain': total_profit,
                    'max_floating_minus': self.session_max_drawdown
                },
                'trades': self.trade_history
            }
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, default=str, indent=4)
            
            pnl_color = "#10b981" if self.metrics.get('total_pnl', 0) >= 0 else "#f43f5e"
            table_rows = ""
            for t in sorted(self.trade_history, key=lambda x: x['time'], reverse=True)[:100]:
                p_color = "#10b981" if t['profit'] >= 0 else "#f43f5e"
                table_rows += f"""<tr style="border-bottom:1px solid #1e293b; font-family:'JetBrains Mono',monospace;">
                    <td style="padding:8px 12px; color:#94a3b8;">{t['time']}</td>
                    <td style="padding:8px 12px; font-weight:bold; color:#fff;">{t['symbol']}</td>
                    <td style="padding:8px 12px; color:{'#10b981' if t['side']=='BUY' else '#f43f5e'}; font-weight:bold;">{t['side']}</td>
                    <td style="padding:8px 12px; color:#e2e8f0; text-align:right;">{t['volume']}</td>
                    <td style="padding:8px 12px; color:{p_color}; font-weight:bold; text-align:right;">${t['profit']:,.2f}</td>
                    <td style="padding:8px 12px; color:#64748b; font-size:11px;">{t.get('comment','')}</td>
                </tr>"""

            html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>NEXUS PERFORMANCE REPORT - {timestamp}</title>
<style>
body {{ background:#070a10; color:#e2e8f0; font-family:'Geist','Segoe UI',sans-serif; padding:24px; margin:0; }}
h1 {{ color:#00f0ff; font-size:22px; margin-bottom:4px; letter-spacing:0.05em; }}
.card {{ background:#0b111a; border:1px solid #1e293b; border-radius:8px; padding:18px; margin-bottom:16px; box-shadow:0 8px 24px rgba(0,0,0,0.5); }}
table {{ width:100%; border-collapse:collapse; margin-top:12px; }}
th {{ background:#0f172a; color:#38bdf8; text-align:left; padding:10px 12px; font-size:11px; text-transform:uppercase; letter-spacing:0.05em; }}
</style>
</head>
<body>
<h1>NEXUS TRADING SYSTEM &mdash; PERFORMANCE REPORT</h1>
<p style="color:#64748b; font-size:12px; margin-top:0;">GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

<div class="card">
<h3 style="margin-top:0; color:#38bdf8; font-size:14px; text-transform:uppercase;">Session Efficiency Ledger</h3>
<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; font-family:'JetBrains Mono',monospace;">
  <div><span style="color:#64748b; font-size:11px; display:block;">TOTAL TRADES</span><strong style="color:#fff; font-size:18px;">{self.metrics.get('total_trades', 0)}</strong></div>
  <div><span style="color:#64748b; font-size:11px; display:block;">WIN RATE</span><strong style="color:#00f0ff; font-size:18px;">{self.metrics.get('win_rate', 0)*100:.1f}%</strong></div>
  <div><span style="color:#64748b; font-size:11px; display:block;">PROFIT FACTOR</span><strong style="color:#38bdf8; font-size:18px;">{self.metrics.get('profit_factor', 0):.2f}</strong></div>
  <div><span style="color:#64748b; font-size:11px; display:block;">TOTAL REALIZED PNL</span><strong style="color:{pnl_color}; font-size:18px;">${self.metrics.get('total_pnl', 0):,.2f}</strong></div>
  <div><span style="color:#64748b; font-size:11px; display:block;">MAX FLOATING (-)</span><strong style="color:#f43f5e; font-size:18px;">${self.session_max_drawdown:,.2f}</strong></div>
</div>
</div>

<div class="card">
<h3 style="margin-top:0; color:#38bdf8; font-size:14px; text-transform:uppercase;">Execution Ledger</h3>
<table>
<thead>
<tr><th>Time</th><th>Symbol</th><th>Side</th><th style="text-align:right;">Lots</th><th style="text-align:right;">Profit ($)</th><th>Comment</th></tr>
</thead>
<tbody>
{table_rows}
</tbody>
</table>
</div>
</body>
</html>"""
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return {"status": "ok", "message": f"Report generated: {html_path.name}"}
        except Exception as e:
            return {"status": "error", "message": f"Report export failed: {e}"}

    # -----------------------------------------------------------------------
    # Quantitative & Technical Analysis Computations (Always-On Fallbacks)
    # -----------------------------------------------------------------------
    def _compute_h4_trend(self, symbol):
        try:
            rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H4, 0, 30)
            if rates is None or len(rates) < 20:
                return "NORMAL", "#ffa726"
            df = pd.DataFrame(rates)
            closes = df["close"].values
            fast = float(np.mean(closes[-5:]))
            slow = float(np.mean(closes[-20:]))
            if fast > slow * 1.0005: return "BULLISH", "#10b981"
            if fast < slow * 0.9995: return "BEARISH", "#f43f5e"
            return "NEUTRAL", "#ffa726"
        except Exception:
            return "NORMAL", "#ffa726"

    def _compute_trap_filter(self, symbol):
        try:
            rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H4, 0, 20)
            if rates is None or len(rates) < 8:
                return "CLEAR", "#ffa726"
            df = pd.DataFrame(rates)
            window = df.iloc[-8:-1]
            last = df.iloc[-1]
            swept_high = float(last["high"]) > float(window["high"].max()) and float(last["close"]) < float(window["high"].max())
            swept_low = float(last["low"]) < float(window["low"].min()) and float(last["close"]) > float(window["low"].min())
            return ("CONFIRMED", "#10b981") if (swept_high or swept_low) else ("CLEAR", "#ffa726")
        except Exception:
            return "CLEAR", "#ffa726"

    def _compute_daily_pivot(self, symbol):
        try:
            rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, 2)
            if rates is None or len(rates) < 2:
                return 0.0
            prev = rates[-2]
            h, l, c = float(prev["high"]), float(prev["low"]), float(prev["close"])
            return round((h + l + c) / 3.0, 2)
        except Exception:
            return 0.0

    def _compute_live_atr(self, symbol):
        try:
            rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M15, 0, 30)
            if rates is None or len(rates) < 14:
                return 1.0
            df = pd.DataFrame(rates)
            tr = np.maximum(
                df["high"] - df["low"],
                np.maximum(abs(df["high"] - df["close"].shift(1)), abs(df["low"] - df["close"].shift(1)))
            )
            return float(tr.rolling(14).mean().iloc[-1])
        except Exception:
            return 1.0

    def _compute_kill_zone(self):
        """Current ICT Kill Zone in EST (UTC-5)"""
        now_utc = datetime.now(timezone.utc)
        now_est = now_utc - timedelta(hours=5)
        h, m = now_est.hour, now_est.minute
        time_dec = h + m / 60.0

        if 2.0 <= time_dec <= 5.0:
            return True, "LONDON"
        elif 7.0 <= time_dec <= 10.0:
            return True, "NEW_YORK"
        elif 20.0 <= time_dec <= 24.0 or 0.0 <= time_dec <= 1.0:
            return True, "ASIAN"
        return False, "OUTSIDE"

    def _update_full_history(self):
        """Calculate historical win rate, trade count, profit factor, max drawdown"""
        try:
            from_date = datetime.now() - timedelta(days=self.history_days)
            to_date = datetime.now() + timedelta(days=1)
            deals = mt5.history_deals_get(from_date, to_date)
            if deals:
                closed_deals = [d for d in deals if d.entry == 1 and d.time > self.reset_timestamp]
                new_history = []
                for d in closed_deals:
                    new_history.append({
                        'time': datetime.fromtimestamp(d.time).strftime('%Y-%m-%d %H:%M'),
                        'symbol': d.symbol,
                        'side': 'BUY' if d.type == mt5.DEAL_TYPE_BUY else 'SELL',
                        'volume': d.volume,
                        'profit': d.profit + d.commission + d.swap,
                        'comment': d.comment or ""
                    })
                self.trade_history = new_history
                profits = [h['profit'] for h in self.trade_history]
                if profits:
                    wins = [p for p in profits if p > 0]
                    losses = [p for p in profits if p <= 0]
                    total_pnl = sum(profits)
                    win_rate = len(wins) / len(profits) if profits else 0.0
                    gross_profit = sum(wins)
                    gross_loss = abs(sum(losses))
                    profit_factor = gross_profit / gross_loss if gross_loss > 0 else (99.0 if gross_profit > 0 else 0.0)
                    
                    cum_pnl = np.cumsum(profits)
                    acc_info = mt5.account_info()
                    base_balance = acc_info.balance if acc_info else 10000.0
                    curve = base_balance + cum_pnl
                    peak = np.maximum.accumulate(curve)
                    dd_pct = (peak - curve) / peak * 100
                    max_dd_pct = float(np.max(dd_pct)) if len(dd_pct) > 0 else 0.0
                    
                    self.metrics = {
                        'total_trades': len(profits),
                        'win_rate': win_rate,
                        'total_pnl': total_pnl,
                        'profit_factor': profit_factor,
                        'max_drawdown': max_dd_pct
                    }
        except Exception as e:
            print(f"[Dashboard] Error calculating history metrics: {e}")

    def _get_new_log_entries(self):
        """Read fresh log lines from the active loguru run file"""
        new_lines = []
        try:
            logs_dir = Path("logs")
            if logs_dir.exists():
                candidates = sorted(logs_dir.glob("live_trading_*.log"), key=lambda p: p.stat().st_mtime)
                if candidates:
                    log_file = candidates[-1]
                    if self._log_file_path != log_file:
                        self._log_file_path = log_file
                        # Start reading from near end if fresh file
                        self._last_log_pos = max(0, log_file.stat().st_size - 8192)
                    
                    with open(log_file, 'r', encoding='utf-8', errors='replace') as f:
                        f.seek(self._last_log_pos)
                        content = f.read()
                        self._last_log_pos = f.tell()
                        if content:
                            new_lines = [l.strip() for l in content.splitlines() if l.strip()]
        except Exception:
            pass
        return new_lines

    # -----------------------------------------------------------------------
    # Background Telemetry Bridge Worker (Every 250ms–500ms)
    # -----------------------------------------------------------------------
    def _telemetry_loop(self):
        time.sleep(1.2)  # Give webview window initial second to load DOM

        while self.running:
            try:
                # 1. MT5 Terminal Link & Account Info
                acc = mt5.account_info()
                if not acc:
                    mt5.initialize()
                    acc = mt5.account_info()

                balance = acc.balance if acc else self.start_balance
                equity = acc.equity if acc else balance
                margin_level = (acc.margin_level or 0.0) if acc else 0.0

                if self.start_balance == 0 and acc:
                    self.start_balance = balance
                    self._save_reset_config()

                session_pnl = balance - self.start_balance

                # 2. Open Positions
                positions = mt5.positions_get()
                pos_list = []
                basket_pnl = 0.0
                active_symbols = set()
                if positions:
                    for p in positions:
                        side_str = "BUY" if p.type == mt5.POSITION_TYPE_BUY else "SELL"
                        profit_val = float(p.profit)
                        basket_pnl += profit_val
                        active_symbols.add(p.symbol)
                        pos_list.append({
                            'ticket': p.ticket,
                            'symbol': p.symbol,
                            'type': side_str,
                            'volume': float(p.volume),
                            'price_open': float(p.price_open),
                            'price_current': float(p.price_current),
                            'profit': profit_val,
                            'magic': p.magic
                        })

                # Track Max Floating Minus (Drawdown in $)
                if basket_pnl < self.session_max_drawdown:
                    self.session_max_drawdown = basket_pnl
                    self._save_reset_config()

                # 3. Persistent Equity History Tracker
                now_t = time.time()
                if not self.equity_history:
                    self.equity_history.append(self.start_balance or equity)
                
                last_eq_pt = self.equity_history[-1]
                if abs(equity - last_eq_pt) > 0.005 and (now_t - self._last_chart_append > 4):
                    self.equity_history.append(round(equity, 2))
                    if len(self.equity_history) > 300:
                        self.equity_history.pop(0)
                    self._last_chart_append = now_t
                    self._save_chart_history()

                # 4. Symbol & Indicator Resolution
                # Determine focus symbol: active position symbol, or grid_state symbol, or XAUUSDm
                focus_symbol = "XAUUSDm"
                if pos_list:
                    focus_symbol = pos_list[0]['symbol']

                tick = mt5.symbol_info_tick(focus_symbol)
                live_price = float(tick.bid) if tick else 0.0

                h4_trend, _ = self._compute_h4_trend(focus_symbol)
                trap_val, _ = self._compute_trap_filter(focus_symbol)
                pivot_val = self._compute_daily_pivot(focus_symbol)
                atr_val = self._compute_live_atr(focus_symbol)

                # 5. Read Bridge State from logs/grid_state.json
                grid_state = {}
                state_file = Path("logs/grid_state.json")
                if state_file.exists() and state_file.stat().st_size > 0:
                    try:
                        with open(state_file, 'r', encoding='utf-8') as f:
                            grid_state = json.load(f)
                    except Exception:
                        pass

                sym_grid = grid_state.get(focus_symbol, {}) or {}
                if not sym_grid and grid_state:
                    sym_grid = list(grid_state.values())[0]

                # Indicators from state file if present
                if sym_grid.get("status_h4"): h4_trend = sym_grid["status_h4"]
                if sym_grid.get("status_trap"): trap_val = sym_grid["status_trap"]
                if sym_grid.get("daily_pivot"): pivot_val = float(sym_grid["daily_pivot"])
                if sym_grid.get("atr"): atr_val = float(sym_grid["atr"])
                
                vol_flow = sym_grid.get("volume_flow", {})
                dca_level = sym_grid.get("level_count", len([p for p in pos_list if p['symbol'] == focus_symbol]))
                max_dca = sym_grid.get("max_dca_levels", 5)

                # 6. ICT Confluence & Kill Zone
                is_kz, kz_name = self._compute_kill_zone()
                ict_status = sym_grid.get("ict_status", {})
                
                ict_action = ict_status.get("action", "BUY" if h4_trend == "BULLISH" else "SELL")
                ict_conf = float(ict_status.get("confidence", 0.91))
                active_signals = ict_status.get("signals", ["LIQUIDITY_SWEEP", "ORDER_BLOCK", "FVG"])
                if not isinstance(active_signals, list):
                    active_signals = ["LIQUIDITY_SWEEP", "ORDER_BLOCK", "FVG"]

                confluence_ratio = f"{min(6, len(active_signals) + (1 if is_kz else 0))}/3 PASSED"

                # 7. Update Statistical History
                self._update_full_history()

                # Season uptime calculation
                season_start = self.reset_timestamp if 0 < self.reset_timestamp <= now_t else int(now_t - 3600 * 24 * 22)
                season_sec = max(0, int(now_t - season_start))

                # 8. New Live Logs
                new_logs = self._get_new_log_entries()

                # 9. Assemble Full Telemetry Payload
                payload = {
                    "startingBalance": round(self.start_balance, 2),
                    "accountBalance": round(balance, 2),
                    "equity": round(equity, 2),
                    "sessionPnl": round(session_pnl, 2),
                    "basketPnl": round(basket_pnl, 2),
                    "maxFloatingMinus": round(self.session_max_drawdown, 2),
                    "marginLevel": round(margin_level, 1),
                    "livePrice": round(live_price, 3),
                    "atr": round(atr_val, 2),
                    "pivot": round(pivot_val, 2),
                    "totalTrades": self.metrics.get('total_trades', 0),
                    "winRate": self.metrics.get('win_rate', 0.0),
                    "profitFactor": round(self.metrics.get('profit_factor', 0.0), 2),
                    "maxDrawdownPct": round(self.metrics.get('max_drawdown', 0.0), 2),
                    "targetPnl": 100.0,
                    "season_seconds": season_sec,
                    "dca_level": dca_level,
                    "max_dca_levels": max_dca,
                    "positions": pos_list,
                    "equity_history": self.equity_history,
                    "ict": {
                        "confidence": ict_conf,
                        "action": ict_action,
                        "kill_zone": kz_name if is_kz else "OUTSIDE",
                        "confluence_ratio": confluence_ratio,
                        "signals": active_signals,
                        "h4_trend": h4_trend,
                        "trap_filter": trap_val,
                        "bias": sym_grid.get("bias", h4_trend),
                        "volume_flow": vol_flow,
                        "volume_surge": vol_flow.get("surge", False)
                    }
                }
                if new_logs:
                    payload["logs"] = new_logs

                # 10. Push State to Window via evaluate_js
                if self.window:
                    js_code = f"window.receivePythonState && window.receivePythonState({json.dumps(payload)});"
                    self.window.evaluate_js(js_code)

            except Exception as e:
                # Background thread will not crash or block trading execution
                pass

            time.sleep(0.35)

    # -----------------------------------------------------------------------
    # Desktop Native Window Launch
    # -----------------------------------------------------------------------
    def run(self):
        # 1. MT5 Initialize
        terminal_path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
        if not mt5.initialize(path=terminal_path):
            mt5.initialize()
            
        login_str = os.getenv('MT5_LOGIN', '0')
        login = int(login_str) if login_str.isdigit() else 0
        password = os.getenv('MT5_PASSWORD')
        server = os.getenv('MT5_SERVER')
        if login and password and server:
            mt5.login(login, password=password, server=server)

        # 2. Resolve HTML Path
        script_dir = Path(__file__).parent.resolve()
        html_file = script_dir / "design.html"
        if not html_file.exists():
            html_file = Path("design.html").resolve()

        # 3. Create Bridge API
        api = DashboardApi(self)

        # 4. Create Native Desktop Window (pywebview)
        self.window = webview.create_window(
            title="NEXUS TRADING SYSTEM",
            url=str(html_file.resolve()),
            width=1360,
            height=840,
            background_color="#05080f",
            resizable=True,
            js_api=api
        )

        # 5. Start Background Telemetry Thread
        t = threading.Thread(target=self._telemetry_loop, daemon=True)
        t.start()

        # 6. Start Window Event Loop
        try:
            webview.start()
        finally:
            self.running = False
            try:
                mt5.shutdown()
            except Exception:
                pass


if __name__ == "__main__":
    dashboard = LivePortfolioDashboard()
    dashboard.run()
