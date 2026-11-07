---
name: Nexus Terminal
colors:
  surface: '#0f131c'
  surface-dim: '#0f131c'
  surface-bright: '#353942'
  surface-container-lowest: '#0a0e16'
  surface-container-low: '#181c24'
  surface-container: '#1c2028'
  surface-container-high: '#262a33'
  surface-container-highest: '#31353e'
  on-surface: '#dfe2ee'
  on-surface-variant: '#bcc9cd'
  inverse-surface: '#dfe2ee'
  inverse-on-surface: '#2c3039'
  outline: '#869397'
  outline-variant: '#3d494c'
  surface-tint: '#4cd7f6'
  primary: '#4cd7f6'
  on-primary: '#003640'
  primary-container: '#06b6d4'
  on-primary-container: '#00424f'
  inverse-primary: '#00687a'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#ffb95f'
  on-tertiary: '#472a00'
  tertiary-container: '#e79400'
  on-tertiary-container: '#563400'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#acedff'
  primary-fixed-dim: '#4cd7f6'
  on-primary-fixed: '#001f26'
  on-primary-fixed-variant: '#004e5c'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb95f'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#0f131c'
  on-background: '#dfe2ee'
  surface-variant: '#31353e'
typography:
  headline-xl:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
  headline-xl-mobile:
    fontFamily: Geist
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 32px
  headline-lg:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  headline-md:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  headline-sm:
    fontFamily: Geist
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 20px
  body-lg:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.06em
  data-mono-num:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: -0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 0.75rem
  gutter-desktop: 1rem
  margin: 0.75rem
  margin-desktop: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1rem
  space-xl: 1.5rem
---

## Brand & Style
The design system operates at the intersection of professional IDE architecture and mission-critical telemetry. Built for institutional quantitative traders, smart money concept (SMC) analysts, and algorithmic systems operators, it conveys precision, uncompromising execution speed, and absolute situational awareness.

The visual style blends modern terminal brutalism with sleek, low-friction IDE layouts. It eliminates gratuitous ornament in favor of data density, high-contrast visual cues, and deterministic spatial grids. Structural surfaces use ultra-dark carbon and slate tones to minimize optic fatigue during sustained market sessions, while glowing indicator lights, telemetry badges, and laser-precise 1px borders guide rapid decision-making across volatile market conditions.

## Colors
The palette is engineered for instantaneous semantic parsing in low-light environments:
- **Primary Cyber Cyan (`#06b6d4`)**: Terminal telemetry, algorithmic execution states, active selections, fair value gaps (FVG), and system hooks.
- **Secondary Emerald (`#10b981`)**: Bullish confirmation, order block mitigation long, long liquidity sweeps, realized profit, and connected nodes.
- **Tertiary Electric Amber (`#f59e0b`)**: System alerts, pending scans, unmitigated imbalance markers, warnings, and pending fill triggers.
- **Critical Crimson (`#ef4444`)**: Bearish bias, short setups, stop losses, invalidation thresholds, and execution failures.
- **Base Surfaces & Carbon Hierarchy**:
  - Root Canvas: `#0b0f17` (Deep Slate Carbon)
  - Surface Panel / Card: `#111827` (Charcoal Slate)
  - Surface Raised / Toolbars: `#1f2937` (Muted Graphite)
  - Border Lines: `#1e293b` (Default) with `#334155` for active panel focus.
  - Text & Numeric Tokens: Primary `#f8fafc`, Secondary `#94a3b8`, Muted `#475569`.

## Typography
The system employs a dual-font structure:
- **Interface & Structure**: Geist provides neutral, razor-sharp structural labels, modal headings, and operational prose without geometric distortion.
- **Telemetry & Numbers**: JetBrains Mono serves all quantitative readouts, price ladders, SMC block coordinate tags, execution latencies, and terminal logs. Tabular lining is strictly enabled across all monospaced values to prevent visual jitter during high-frequency price updates.
- All uppercase monospaced labels (`label-sm`, `label-md`) strictly incorporate positive letter spacing to maintain rapid scanability against dark backdrops.

## Layout & Spacing
The layout follows a modular IDE workbench model built around high-density, docked dockable panels and multi-split panes:
- **Grid Architecture**: 24-column flexible grid with persistent 0px-collapse divider seams or fixed 12px/16px gutters depending on operational view (terminal mode vs. macro telemetry dashboard).
- **Density Profile**: Tight spatial baseline (4px sub-grid) maximizing above-the-fold screen real estate. Panel headers, status strips, and tabular telemetry rows use compact vertical paddings (`space-xs` and `space-sm`).
- **Breakpoints & Adaptability**:
  - `Desktop (>= 1280px)`: Full multi-pane arrangement (Order Book, Market Structure Tree, Live Candlestick/FVG Heatmap, Algo Execution Queue).
  - `Tablet (768px - 1279px)`: Split-pane stack with tabbed telemetry docks.
  - `Mobile (< 768px)`: Single active view with fixed bottom telemetry dock and sliding drawer diagnostics.

## Elevation & Depth
Depth is rendered through structural tonal hierarchy and razor-thin borders, avoiding diffuse real-world dropshadows:
- **Tonal Stepping**: Baseline canvas (`#0b0f17`) hosts primary modular frames (`#111827`), which stack internal data cards and code blocks (`#172033`).
- **Border-Defined Structure**: Visual boundary definition relies on 1px solid borders (`#1e293b`). Hover and selected states shift border hues to Cyber Cyan (`#06b6d4`) or active state accents.
- **Telemetry Glows**: High-priority events (e.g., Fair Value Gap tap, liquidity sweep triggered) employ focused, chromatic glow drops: `0 0 12px rgba(6, 182, 212, 0.35)` or `0 0 12px rgba(16, 185, 129, 0.35)`.
- **Modals & Overlays**: Backdrop filtering applies `backdrop-filter: blur(8px)` with a 75% dark tint overlay (`rgba(11, 15, 23, 0.75)`) and a crisp `1px solid #334155` border envelope.

## Shapes
Geometry is disciplined, utilitarian, and engineered:
- Level 1 (`0.25rem` / 4px corner radius) standardizes all interactives: buttons, inputs, badge tags, pane corners, and table row selections.
- Key telemetry chips and status pill lights utilize 9999px pill radii strictly for standalone system state pings.
- Panels in the main workbench can optionally use 0px outer corners to achieve an edge-to-edge IDE interface appearance.

## Components

### Buttons
- **Action / Execution Primary**: Cyan background (`#06b6d4`), deep slate text (`#080d14`), font `JetBrains Mono` 12px weight 600, 4px border radius. Hover: `#22d3ee` with cyan focus ring.
- **Bullish Execution (Buy / Long)**: Emerald background (`#10b981`), black text, monospaced weight 600.
- **Bearish Execution (Sell / Short)**: Crimson background (`#ef4444`), white text, monospaced weight 600.
- **Terminal Ghost / Utility**: Background transparent, border `1px solid #1e293b`, text `#94a3b8`. Hover: background `#1f2937`, text `#f8fafc`.

### Chips & Telemetry Badges
- **Status Badges**: Monospace text (`label-sm`), 4px radius, padded with 2px vertical / 6px horizontal. Semitransparent fill (`rgba(accent, 0.12)`) and matching 1px border (`rgba(accent, 0.3)`).
- **Live Indicator Ping**: 6px circular dot with concentric pulse ring animation signaling active WebSocket telemetry.

### Inputs & Command Line Box
- **Query / Param Inputs**: Background `#0f172a`, border `1px solid #1e293b`, font `JetBrains Mono` 13px. Focus states trigger border `#06b6d4` with zero ambient blur, matching code editors.
- **Monospace Value Stepper**: Inline suffix flags (e.g., `LOTS`, `TICKS`, `USDT`) rendered in muted slate (`#475569`).

### Data Tables & Structured Telemetry Lists
- **Rows**: Alternating subtle zebra striping (`#111827` and `#0e1420`). Border-bottom 1px solid `#1e293b`.
- **Metrics Layout**: Right-aligned numeric columns using `JetBrains Mono`. Color-coded spreads: positive figures in `#10b981`, negative in `#ef4444`.
- **Selection State**: Left border accent 2px solid `#06b6d4` with row background tint `rgba(6, 182, 212, 0.05)`.

### Checkboxes, Switches & Radio Controls
- **Checkboxes**: 14x14px square, 2px radius, border `1px solid #334155`. Checked state: `#06b6d4` fill with jet black checkmark glyph.
- **Toggle Switches**: Compact rectangular housing (28x16px), 2px radius. Active state thumb shifts right with emerald fill for active automated bots.

### Cards & Analytical Panels
- Header toolbar height pinned to 32px with uppercase monospaced section title, live latency counter, and pane action icons (minimize, split, detach).
- Card container body uses background `#111827` with 1px border `#1e293b`.