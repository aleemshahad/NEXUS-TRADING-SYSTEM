# SKILL: `nexus_brand_kit_v1`
**Brand Name:** NEXUS AUTOMATION  
**Founder:** Aleem Shahzad (Tech-Driven SEO Expert, Full-Stack Developer & Automation Specialist)  
**Location:** Lodhran, Pakistan  
**Public Contact Rule:** **STRICTLY** use `aleemsssg@gmail.com` on all public banners, social posts, UI footers, and watermarks. **NEVER** display personal phone or WhatsApp numbers unless explicitly instructed for a specific private deliverable.

---

## 1. Brand Positioning & Tone of Voice (`skill:brand_voice`)
* **Archetype:** The Systems Architect — where Python/CDP Automation meets Data-Driven SEO & Full-Stack Engineering.
* **Visual Vibe:** Dark-Mode Command Center, Terminal Precision, High-Contrast Data Visualization.
* **Language & Copy Style:** Practical-smart, authoritative, zero fluff. Supports pure English or natural Pakistani Freelancer/Community Roman Urdu + English (Hinglish) mix.
* **Code & Terminal Output Rule:** Inside code blocks and terminal logs, strictly use English or Roman Urdu (never pure Urdu script).
* **Core Taglines:**
  * *"Automate the Workflow. Dominate the SERPs."*
  * *"Autonomous Systems. Measurable SEO Growth."*
  * *"Engineered SEO & Custom Python Automation."*
* **CTA Strategy:** Value-first, metric-led proof (Ahrefs DR, traffic upticks, execution speed, zero-cost self-hosted efficiency) followed by a soft CTA directing to `aleemsssg@gmail.com`.

---

## 2. Master Color Palette & CSS Tokens (`skill:color_tokens`)

 integrates both the **Command-Center UI Palette** (for web apps, dashboards, and social carousels) and the **Logo Vector Palette** (for emblems and 3D/AI renders).

| Token Role | Name | Hex | RGB | CMYK (Print) | Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `--nx-bg-void` | Obsidian Void | `#0B0F19` | `11, 15, 25` | `85, 75, 55, 80` | Primary canvas & dark background (60%) |
| `--nx-bg-slate` | Deep Slate Navy | `#0F172A` | `15, 23, 42` | `82, 71, 48, 65` | Logo backdrop & secondary hero sections |
| `--nx-surface` | Terminal Slate | `#111827` | `17, 24, 39` | `80, 70, 50, 70` | Elevated cards, code blocks, metric containers |
| `--nx-cyan-neon` | Cyber Cyan | `#00F5D4` | `0, 245, 212` | `65, 0, 28, 0` | Primary UI accent, key nodes, active states |
| `--nx-cyan-elec` | Electric Cyan | `#38BDF8` | `56, 189, 248` | `68, 14, 0, 0` | Logo top-left gradient & circuit glow |
| `--nx-blue-royal` | Royal Blue | `#2563EB` | `37, 99, 235` | `85, 62, 0, 0` | Logo bottom-right gradient & deep accents |
| `--nx-emerald` | Signal Emerald | `#10B981` | `16, 185, 129` | `78, 0, 58, 0` | SEO traffic upticks, positive ROI, live badges |
| `--nx-text-main` | Crisp Titanium | `#F8FAFC` | `248, 250, 252` | `2, 1, 0, 0` | Primary headlines & high-contrast body text |
| `--nx-text-muted` | Muted Steel | `#94A3B8` | `148, 163, 184` | `42, 29, 18, 3` | Subtitles, axis labels, secondary metadata |

### Drop-in CSS / Tailwind Variables
```css
:root {
  --nx-bg-void: #0B0F19;
  --nx-bg-slate: #0F172A;
  --nx-surface: #111827;
  --nx-border: rgba(248, 250, 252, 0.12);
  --nx-cyan-neon: #00F5D4;
  --nx-cyan-elec: #38BDF8;
  --nx-blue-royal: #2563EB;
  --nx-emerald: #10B981;
  --nx-text-main: #F8FAFC;
  --nx-text-muted: #94A3B8;
  --nx-gradient-logo: linear-gradient(135deg, #38BDF8 0%, #00F5D4 45%, #2563EB 100%);
  --nx-shadow-glow: 0 0 24px rgba(0, 245, 212, 0.22);
}
```

---

## 3. Typography System (`skill:typography`)

1. **Headlines & Hooks:** `Space Grotesk` (or `Plus Jakarta Sans`)
   * **Weights:** Bold (`700`), ExtraBold (`800`)
   * **Tracking:** `-0.02em` (tight, engineered feel)
   * **Use Case:** Carousel titles, banner hooks, section headers.
2. **Body & UI Controls:** `Inter`
   * **Weights:** Regular (`400`), Medium (`500`), SemiBold (`600`)
   * **Line Height:** `1.5` to `1.6`
   * **Use Case:** Case study paragraphs, dashboard labels, documentation.
3. **Technical, Code & Metrics:** `JetBrains Mono`
   * **Weights:** Medium (`500`), Bold (`700`)
   * **Use Case:** Terminal outputs, Python/CDP snippets, ROI numbers (`+247%`), and the mandatory footer signature `aleemsssg@gmail.com`.

---

## 4. Scalable Vector Logo Code (`skill:svg_logo`)

Copy and save this block as `nexus-logo.svg` for infinite resolution across web apps, favicons, and print media:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="nxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#00F5D4" />
      <stop offset="100%" stop-color="#2563EB" />
    </linearGradient>
    <filter id="nxGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="512" height="512" rx="96" fill="#0F172A" />

  <!-- Subtle Dot Matrix Grid -->
  <pattern id="dotGrid" width="24" height="24" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#38BDF8" fill-opacity="0.12" />
  </pattern>
  <rect width="512" height="512" rx="96" fill="url(#dotGrid)" />

  <!-- Interconnected Geometric 'N' -->
  <g filter="url(#nxGlow)">
    <!-- Left Vertical & Diagonal Outer Track -->
    <path d="M144 384 V128 L328 312 V128" fill="none" stroke="url(#nxGrad)" stroke-width="28" stroke-linecap="square" stroke-linejoin="miter" />
    <!-- Right Vertical & Inner Parallel Track -->
    <path d="M368 128 V384 L184 200 V384" fill="none" stroke="url(#nxGrad)" stroke-width="20" stroke-linecap="square" stroke-linejoin="miter" opacity="0.85" />
    <!-- Central Automation Routing Node -->
    <line x1="216" y1="296" x2="296" y2="216" stroke="#00F5D4" stroke-width="8" stroke-linecap="round" />
    <circle cx="256" cy="256" r="16" fill="#0B0F19" stroke="#00F5D4" stroke-width="8" />
    <circle cx="256" cy="256" r="6" fill="#F8FAFC" />
    <circle cx="212" cy="300" r="6" fill="#38BDF8" />
    <circle cx="300" cy="212" r="6" fill="#38BDF8" />
  </g>
</svg>
```

---

## 5. All-Media Specification Matrix (`skill:media_specs`)

Use these exact dimensions and color spaces when generating or exporting assets for any platform:

### A. Digital & Social Media (`RGB`, `72–144 DPI`, `.PNG` / `.WEBP` / `.MP4`)
* **LinkedIn Personal Banner:** `1584 x 396 px` (Keep left `350px` clear for profile photo overlap; place headline center-right and `aleemsssg@gmail.com` bottom-right).
* **X (Twitter) Header Banner:** `1500 x 500 px` (Safe zone centered vertically).
* **LinkedIn / Instagram Carousel (Portrait):** `1080 x 1350 px` (`4:5` ratio — highest feed real estate).
* **Binance Square / X Single Post:** `1200 x 675 px` (`16:9` ratio) or `1080 x 1080 px` (`1:1`).
* **YouTube Shorts / Reels Overlay:** `1080 x 1920 px` (`9:16` vertical, keep bottom `25%` clear of UI captions).
* **Profile Avatar / App Icon:** `512 x 512 px` and `1024 x 1024 px` (Icon-only geometric `N`, no subtext).
* **Web Favicons:** `16x16`, `32x32`, `180x180` (`apple-touch-icon.png`), and `.ICO` / `.SVG`.

### B. Document & Presentation Templates (`RGB`, `.PDF` / `.PPTX` / `.DOCX` / `.HTML`)
* **Pitch Deck / Case Study Slides:** `1920 x 1080 px` (`16:9` Widescreen).
* **SEO Audit & Automation Proposal / Invoice:** `A4` (`210 x 297 mm`) with dark header strip (`#0B0F19`) and clean light body (`#F8FAFC`) for ink-friendly printing if needed.

### C. Print & Physical Merchandise (`CMYK`, `300 DPI`, `.AI` / `.EPS` / `.PDF` with `3mm` bleed)
* **Business Card:** `3.5 x 2 in` (`88.9 x 50.8 mm`) — Matte black/obsidian lamination with Spot UV gloss on the geometric `N` logo.
* **Event Roll-Up Standee:** `850 x 2000 mm` (`150–300 DPI`).
* **Apparel / Hoodies / Mugs:** Vector knockout (`.SVG` / `.EPS`) in 3-color screen print or metallic cyan/white embroidery on dark navy fabric.

---

## 6. AI Image Generator Prompts Library (`skill:ai_prompts`)

### 1. Primary Logo Mark Prompt
> `A minimalist, futuristic tech logo for an automation agency named "NEXUS". The centerpiece is a sleek, interconnected geometric letter "N" formed with sharp angles and clean lines, featuring a glowing electric cyan (#38bdf8) and deep royal blue (#2563eb) gradient. A subtle glowing automation node sits at the core intersection. Set against a clean, dark slate navy background (#0f172a). Modern corporate identity style, vector aesthetics, crisp edges, high contrast, professional lighting, 8k resolution --no realistic photo clutter`

### 2. LinkedIn / X Header Banner Background Prompt
> `Ultra-wide dark-mode futuristic command center background for a tech brand banner, deep obsidian void (#0B0F19) and slate navy (#0F172A) canvas, subtle glowing cyber cyan (#00F5D4) circuit pathways and data routing nodes on the right edge, clean empty negative space on the center and left for typography, minimalist glassmorphism UI grid, 8k vector engineering aesthetic --ar 4:1`

### 3. SEO & Python Case Study Thumbnail Background
> `Dark mode data visualization card background, obsidian slate (#111827) surface with a subtle glowing signal emerald (#10B981) upward trend graph line and cyber cyan (#00F5D4) network nodes, clean glassmorphic border, high-tech minimalist SaaS UI aesthetic, 8k --ar 16:9`

---

## 7. Reusable UI Component Snippet (`skill:html_card_template`)

Drop this self-contained HTML/CSS snippet into any dashboard, Elementor custom HTML block, or social screenshot generator to render an authentic **Nexus Automation Metric Card**:

```html
<div style="background:#0B0F19; padding:32px; font-family:'Inter',sans-serif; color:#F8FAFC; max-width:480px; border-radius:16px; border:1px solid rgba(56,189,248,0.2); box-shadow:0 12px 32px rgba(0,0,0,0.6);">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
    <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00F5D4; background:rgba(0,245,212,0.1); padding:4px 10px; border-radius:6px; border:1px solid rgba(0,245,212,0.3);">
      ● NEXUS_CDP_ENGINE // ACTIVE
    </span>
    <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#94A3B8;">v2.4</span>
  </div>
  
  <h3 style="font-family:'Space Grotesk',sans-serif; font-size:24px; font-weight:700; margin:0 0 8px 0; letter-spacing:-0.02em;">
    Automated SEO & Lead Pipeline
  </h3>
  <p style="font-size:14px; color:#94A3B8; margin:0 0 24px 0; line-height:1.5;">
    Zero-cost self-hosted Python + CDP workflow executing real-time Ahrefs metrics & backlink outreach.
  </p>

  <div style="background:#111827; padding:16px; border-radius:12px; border:1px solid rgba(248,250,252,0.08); display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
    <div>
      <div style="font-size:12px; color:#94A3B8;">ORGANIC TRAFFIC GROWTH</div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:28px; font-weight:700; color:#10B981;">+247.8% ↑</div>
    </div>
    <div style="text-align:right;">
      <div style="font-size:12px; color:#94A3B8;">MANUAL HOURS SAVED</div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:20px; font-weight:700; color:#38BDF8;">38h / wk</div>
    </div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; padding-top:12px; border-top:1px solid rgba(248,250,252,0.08); font-family:'JetBrains Mono',monospace; font-size:12px;">
    <span style="color:#F8FAFC; font-weight:600;">NEXUS AUTOMATION</span>
    <span style="color:#00F5D4;">aleemsssg@gmail.com</span>
  </div>
</div>
```

---

## 8. AI Assistant Execution Rules (`skill:invocation_rules`)
Whenever Aleem invokes **`nexus_brand_kit_v1`** (or asks for a Nexus Automation post, banner, web UI, deck, or script):
1. Apply the **Obsidian Void (`#0B0F19`)**, **Deep Slate (`#0F172A`)**, **Cyber Cyan (`#00F5D4`)**, and **Signal Emerald (`#10B981`)** color scheme automatically.
2. Pair `Space Grotesk` headlines with `Inter` body text and `JetBrains Mono` metrics/terminal logs.
3. Keep all copy practical-smart, metric-driven, and free of generic sales fluff.
4. Always place `aleemsssg@gmail.com` as the public contact identifier and omit phone/WhatsApp numbers unless explicitly requested.