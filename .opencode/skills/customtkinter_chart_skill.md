# customtkinter_chart_skill — Tkinter + Matplotlib Chart Rules

Reusable rules to avoid the common CustomTkinter + Matplotlib bugs
(dead-space canvas, clipped right-edge labels, fake heartbeat data points).

## 1. Zero Dead-Space Canvas Layout (Full Bleed Fit)

- Never hide sizing issues by just painting empty frame space with a dark
  background color. The chart canvas widget MUST physically stretch to fill
  100% of its parent `CTkFrame`.
- Parent frame configuration:
  - `chart_frame.grid_rowconfigure(1, weight=1)` (row 0 = title label, row 1 = canvas)
  - `chart_frame.grid_columnconfigure(0, weight=1)`
  - Place `FigureCanvasTkAgg` widget with
    `grid(row=1, column=0, sticky="nsew", padx=6, pady=(2, 6))` (or
    `pack(fill="both", expand=True, ...)`).
- Matplotlib figure margins (no default large margins):
  - `fig.subplots_adjust(left=0.10, right=0.96, top=0.92, bottom=0.14)`
    (dashboard variant: `left=0.11, right=0.96, top=0.90, bottom=0.14`)
- Bind `<Configure>` on the canvas (and its parent frame) to dynamically
  resize `fig.set_size_inches(event.width / fig.dpi, event.height / fig.dpi)`
  and call `canvas.draw_idle()` so there is zero empty gap on right/bottom.
- Keep annotations/labels inside the plot area:
  - Use `transform=ax.transAxes`, e.g. live equity badge at
    `(x=0.97, y=0.92, ha="right")` so text is never clipped at the right edge.

## 2. Data-Driven Equity Curve + Pulsing Endpoint Beacon (Heartbeat)

- **Strict Rule for Curve Line:** NEVER append new data points to the equity
  curve on a timer if the actual Equity / PnL has not changed. The line
  history must ONLY add a point when a real trade update or PnL change occurs.
- **Strict Rule for Heartbeat (Endpoint Dot Only):**
  - Marker strictly at the LAST point `(x_data[-1], y_data[-1])`.
  - Two markers at the endpoint:
    1. `endpoint_core`: solid dot (`marker="o"`, `markersize=6`,
       `alpha=1.0`, `zorder=6`).
    2. `endpoint_halo`: outer pulse ring (`marker="o"`, `markersize=12`,
       `alpha=0.4`, `zorder=5`).
  - Every 10 seconds, animate ONLY `endpoint_halo` (expanding `markersize`,
     fading `alpha`) at the last point — do NOT append fake points to the line.

## 3. Reference Implementation (adapt names to the host class)

```python
# Initialize once on the chart axes:
(self.equity_line,) = self.ax.plot(
    self.x_data, self.y_data, color="#ff3b5c", linewidth=2, zorder=4
)
(self.endpoint_core,) = self.ax.plot(
    [self.x_data[-1]], [self.y_data[-1]],
    marker="o", markersize=6, color="#ff3b5c", zorder=6,
)
(self.endpoint_halo,) = self.ax.plot(
    [self.x_data[-1]], [self.y_data[-1]],
    marker="o", markersize=12, color="#ff3b5c", alpha=0.4, zorder=5,
)

# Call ONLY when real Equity / PnL changes:
def update_equity_curve(self, new_equity):
    if not self.y_data or abs(self.y_data[-1] - new_equity) > 1e-5:
        next_x = (self.x_data[-1] + 1) if self.x_data else 0
        self.x_data.append(next_x)
        self.y_data.append(new_equity)
        self.equity_line.set_data(self.x_data, self.y_data)
        self.endpoint_core.set_data([self.x_data[-1]], [self.y_data[-1]])
        self.endpoint_halo.set_data([self.x_data[-1]], [self.y_data[-1]])
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw_idle()

# Heartbeat pulse ONLY on the endpoint dot (every 10s):
def trigger_endpoint_heartbeat(self, step=0):
    if not self.x_data:
        return
    last_x, last_y = [self.x_data[-1]], [self.y_data[-1]]
    self.endpoint_core.set_data(last_x, last_y)
    self.endpoint_halo.set_data(last_x, last_y)
    pulse_frames = [(10, 0.65), (14, 0.45), (18, 0.25), (22, 0.10), (10, 0.35)]
    if step < len(pulse_frames):
        size, alpha = pulse_frames[step]
        self.endpoint_halo.set_markersize(size)
        self.endpoint_halo.set_alpha(alpha)
        self.canvas.draw_idle()
        self.after(80, lambda: self.trigger_endpoint_heartbeat(step + 1))
    else:
        self.after(10000, lambda: self.trigger_endpoint_heartbeat(0))
```

## 4. Applied To

- `live_dashboard.py` — "PERFORMANCE CURVE (EQUITY)" card
  (`FigureCanvasTkAgg`, `_render_curve`, `_update_loop` equity append).
