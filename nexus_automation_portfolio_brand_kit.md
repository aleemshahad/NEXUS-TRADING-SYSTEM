
# SKILL: `nexus_brand_kit_v2` (Integrated GitHub Portfolio & Command Center)

**Brand Name:** NEXUS AUTOMATION

**Operator / Founder:** Aleem Shahzad (AI-Augmented Full-Stack Developer & Automation Specialist)

**Location:** Pakistan

**Primary Portfolio URL:** `https://aleemshahad.github.io/portfolio/`

**GitHub Profile:** `https://github.com/aleemshahad`

**Public Contact Rule:** **STRICTLY** use `aleemsssg@gmail.com` on all public banners, social posts, UI footers, and watermarks. **NEVER** display personal phone or WhatsApp numbers on public creative assets.

## 1. Portfolio Architectural Philosophy & Voice (`skill:portfolio_vibe`)

* **Archetype:** The Systems Architect & Full-Stack Operator.

* **Core Concept:** *"Five systems. One operator."* — Treating software engineering, automation, SEO, and content infrastructure as a unified, terminal-driven command center.

* **Tone of Voice:** Engineering-first, hyper-pragmatic, zero fluff, and metric-obsessed. Combines fluent English with natural Pakistani developer community vernacular (Hinglish/Roman Urdu) inside discussions, while keeping all code, terminal logs, and system specs strictly in rigorous English.

* **Core Taglines:**

  * *"Automate the Workflow. Dominate the SERPs."*

  * *"Autonomous Systems. Measurable SEO Growth."*

  * *"Five systems. One operator."*

## 2. Master Color Palette & CSS Tokens (`skill:color_tokens`)

The exact color tokens extracted from your high-contrast dark-mode command center UI:

| Token Role | Name | Hex Code | RGB | Usage | 
| ----- | ----- | ----- | ----- | ----- | 
| `--nx-bg-void` | Obsidian Void | `#0B0F19` | `11, 15, 25` | Primary canvas & dark background (60%) | 
| `--nx-bg-slate` | Deep Slate Navy | `#0F172A` | `15, 23, 42` | Hero sections & container surfaces | 
| `--nx-surface` | Terminal Slate | `#111827` | `17, 24, 39` | Elevated cards, CLI panels, metric blocks | 
| `--nx-cyan-neon` | Cyber Cyan | `#00F5D4` | `0, 245, 212` | Active state indicators, primary accent glow | 
| `--nx-cyan-elec` | Electric Cyan | `#38BDF8` | `56, 189, 248` | Code syntax, subheaders, logo gradient top | 
| `--nx-blue-royal` | Royal Blue | `#2563EB` | `37, 99, 235` | Deep structural borders & logo gradient bottom | 
| `--nx-emerald` | Signal Emerald | `#10B981` | `16, 185, 129` | Growth stats, uptime badges, traffic upticks | 
| `--nx-text-main` | Crisp Titanium | `#F8FAFC` | `248, 250, 252` | Primary headlines and high-contrast copy | 
| `--nx-text-muted` | Muted Steel | `#94A3B8` | `148, 163, 184` | CLI metadata, descriptions, axis labels | 

### Drop-In CSS Variables

```
:root {
  --nx-bg-void: #0B0F19;
  --nx-bg-slate: #0F172A;
  --nx-surface: #111827;
  --nx-border: rgba(56, 189, 248, 0.15);
  --nx-cyan-neon: #00F5D4;
  --nx-cyan-elec: #38BDF8;
  --nx-blue-royal: #2563EB;
  --nx-emerald: #10B981;
  --nx-text-main: #F8FAFC;
  --nx-text-muted: #94A3B8;
  --nx-font-heading: 'Space Grotesk', sans-serif;
  --nx-font-body: 'Inter', sans-serif;
  --nx-font-mono: 'JetBrains Mono', monospace;
}

```

## 3. The 5 Pillars & Operator Lifecycle (`skill:five_systems`)

Every project, portfolio showcase, or proposal must align with your five primary operational domains:

1. **Python & CDP Automation:** Custom browser automation, web scraping, multi-threading, and self-hosted workflow engines (`playwright`, `selenium`, `asyncio`).

2. **Data-Driven SEO Systems:** Programmatic SEO, technical audits, Ahrefs metric scaling, and automated backlink outreach pipelines.

3. **Full-Stack Engineering:** Scalable web apps, modern APIs, high-performance database architectures, and clean UI components.

4. **Social & Content Systems:** Automated publishing loops, multi-platform content distribution across X, LinkedIn, and Binance Square.

5. **Video & Visual Engineering:** Automated video editing workflows, YouTube shorts optimization, and high-retention thumbnail frameworks.

**Operator Lifecycle Rail Format:**
`01 · BOOT` $\rightarrow$ `02 · PROOF` $\rightarrow$ `03 · BUILD` $\rightarrow$ `04 · SHIP` $\rightarrow$ `05 · DEPLOY`

## 4. Typography Hierarchy (`skill:typography`)

* **Headlines & Banners (`Space Grotesk` / `Plus Jakarta Sans`):** Bold (`700`), ExtraBold (`800`). Tight tracking (`-0.02em`) for maximum mobile feed stopping power.

* **Body & UI (`Inter`):** Regular (`400`) & Medium (`500`). Clean legibility at micro scales.

* **CLI, Metrics & Code (`JetBrains Mono`):** Used exclusively for terminal commands (`$ python3 agent.py`), stats (`+247.8%`), repository tags (`21 repos | 58 stars`), and contact info (`aleemsssg@gmail.com`).

## 5. Reusable CLI Proof Card HTML Component (`skill:cli_card`)

Use this block for generating interactive portfolio cards, GitHub README badges, or case-study UI mocks:

```
<div style="background:#0B0F19; padding:28px; font-family:'Inter',sans-serif; color:#F8FAFC; max-width:520px; border-radius:16px; border:1px solid rgba(56,189,248,0.2); box-shadow:0 16px 40px rgba(0,0,0,0.7);">
  <!-- CLI Header Bar -->
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px; border-bottom:1px solid rgba(248,250,252,0.08); padding-bottom:10px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <span style="width:10px; height:100px; background:#00F5D4; border-radius:50%; display:inline-block; box-shadow:0 0 8px #00F5D4;"></span>
      <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00F5D4; letter-spacing:0.05em;">nexus_core // live_terminal</span>
    </div>
    <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#94A3B8;">github.com/aleemshahad</span>
  </div>

  <!-- Terminal Execution Stream -->
  <div style="background:#111827; padding:14px; border-radius:8px; font-family:'JetBrains Mono',monospace; font-size:12px; color:#38BDF8; margin-bottom:16px; border:1px solid rgba(248,250,252,0.05);">
    <span style="color:#94A3B8;">$</span> python3 run_automation.py --target=serp_domination<br>
    <span style="color:#10B981;">[OK]</span> CDP Session active on port 9222<br>
    <span style="color:#10B981;">[OK]</span> Extracted 4,200 targeted SERP nodes
  </div>

  <!-- Headline & Metrics -->
  <h3 style="font-family:'Space Grotesk',sans-serif; font-size:22px; font-weight:700; margin:0 0 6px 0; letter-spacing:-0.02em;">
    Five Systems. One Operator.
  </h3>
  <p style="font-size:13px; color:#94A3B8; margin:0 0 20px 0; line-height:1.5;">
    Custom Python engineering paired with data-driven SEO workflows to scale organic reach without human bottlenecks.
  </p>

  <!-- Metrics Grid -->
  <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-bottom:20px;">
    <div style="background:#111827; padding:12px; border-radius:8px; border:1px solid rgba(248,250,252,0.06);">
      <div style="font-size:11px; color:#94A3B8; font-family:'JetBrains Mono',monospace;">REPOS / STARS</div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:20px; font-weight:700; color:#00F5D4;">21 / 58</div>
    </div>
    <div style="background:#111827; padding:12px; border-radius:8px; border:1px solid rgba(248,250,252,0.06);">
      <div style="font-size:11px; color:#94A3B8; font-family:'JetBrains Mono',monospace;">ORGANIC GROWTH</div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:20px; font-weight:700; color:#10B981;">+247% ↑</div>
    </div>
  </div>

  <!-- Footer ID -->
  <div style="display:flex; justify-content:space-between; align-items:center; padding-top:10px; border-top:1px solid rgba(248,250,252,0.08); font-family:'JetBrains Mono',monospace; font-size:11px;">
    <span style="color:#F8FAFC;">NEXUS AUTOMATION</span>
    <span style="color:#00F5D4;">aleemsssg@gmail.com</span>
  </div>
</div>

```

## 6. AI Invocation & Generation Rules (`skill:invocation_rules`)

When generating content, code, or social assets under **`nexus_brand_kit_v2`**:

1. **Visual Style:** Always use dark-mode command center styling (`#0B0F19` void, `#111827` surface, `#00F5D4` cyan, `#10B981` emerald).

2. **Typography:** Match `Space Grotesk` headers with `Inter` body text and `JetBrains Mono` code/stats.

3. **Identity & Links:** Always credit Aleem Shahzad, point to `https://aleemshahad.github.io/portfolio/`, and output `aleemsssg@gmail.com` as the sole public contact point.