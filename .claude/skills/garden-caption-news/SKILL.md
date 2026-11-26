---
name: garden-caption-news
description: Direct, script, and produce high-retention "Caption News" video explainers and shorts tailored for the US Gardening niche (American home gardeners 35–60+, mobile-first). Features bold sound-off English captions with keyword highlight blocks, Tier A Land-Grant University Extension research proof (Penn State, Cornell, UF IFAS, Texas A&M, USDA), garden myth busting, and zero-dollar Lazy Grandma solutions.
---

# Garden Caption News (US Gardening Edition)

Produces social video news and explainers designed specifically for **American home gardeners aged 35–60+** (core mobile viewers 60–80). Every video is built to be 100% understandable with the **sound off**, driven by huge, high-contrast English captions and rigorous University Extension proof.

Brand Voice: **"Lazy Grandma Wisdom meets Science-Backed Proof"** (reassuring educator, practical, zero fluff, low effort, anti-alarmist).

---

## 1. When to Use

Use this skill when:
- Creating a **Garden Myth-Buster** (e.g. why Epsom salt / baking soda / sugar spray damages soil or plants).
- Creating a **Research Proof Explainer** (e.g. testing popular rooting hacks, fertilizer claims, pruning methods using university bulletins).
- Creating a **Seasonal Urgent Fix** (e.g. frost prep, fall leaf mulching, over-wintering houseplants, pruning deadlines).
- Creating a **Zero-Cost Backyard Hack** (saving money, recycling kitchen waste, simple DIY tools).

---

## 2. Core Constraints for US Gardening (Ages 35–60+)

| Rule | Requirement | Why |
|---|---|---|
| **Language** | 100% US English | Target audience is US domestic gardeners. No bilingual or Chinese text. |
| **Pacing** | **130 – 145 WPM** (Narration) | Calm, unhurried, authoritative grandma/grandpa educator. Avoid rapid TikTok speed. |
| **Caption Time** | Minimum **2.5s – 3.2s** per card | Older eyes require extra reading buffer on mobile screens. |
| **Typography** | `Inter`, `Montserrat`, `Oswald` (80–88px) | Ultra-crisp, high contrast over dark soil canvas (`#121612`). |
| **Highlighting** | One `{keyword}` per card | Colored pill highlight: Pollen Yellow (`#F9C846`) for wins, Coral (`#E53935`) for errors, Green (`#689F38`) for cures. |
| **Safety & YMYL** | Strict Tier A Sources + ASPCA check | Never suggest harmful chemicals (bleach, unbuffered vinegar) or pet toxins. |

---

## 3. Four-Beat Narrative Structure

1. **Frame 4 Hook (0 – 6s)**:
   - Giant quantified figure or shocking mistake rolls to its value in <0.4s.
   - Example: *"73% of gardeners cut back hydrangeas|in late October.|{You just killed next year's blooms}."*
2. **The Turn / The Freeze (6 – 15s)**:
   - Music halts into garden ambient silence.
   - A bold question or freeze frame: *"So why does everyone recommend it?"*
3. **The University Extension Proof (15 – 35s)**:
   - Official Extension bulletin page appears (e.g. `Penn State Extension · Dept of Horticulture`).
   - Neon highlighter sweeps across the key sentence showing the biological mechanism.
   - The verified metric pops out in a clean data card.
4. **The Lazy Grandma Fix (35 – 55s)**:
   - Practical, low-effort action step.
   - Cost comparison card: Commercial chemical fix ($35) vs University-approved zero-dollar lazy method ($0).
   - Reassuring verdict caption card over thriving garden footage.

---

## 4. Source Hierarchy (Tier A Only)

Always cite the exact institution in the top-left **Source Tag**:
- **Land-Grant Universities**: `Penn State Extension`, `Univ. of Florida IFAS`, `Texas A&M AgriLife`, `Cornell Cooperative Extension`, `UC Davis / UC ANR`, `Clemson Extension`, `Univ. of Minnesota Extension`.
- **Federal**: `USDA-ARS`, `USDA Hardiness Zone Map 2023`, `EPA Agricultural Bulletins`.
- **Pet Safety**: `ASPCA Animal Poison Control (APCC)`.

---

## 5. Timeline JSON Format

When generating `timeline.json` for rendering in `styles/caption-news`:

```json
{
 "note": "Garden Caption News timeline for US market",
 "fps": 30,
 "dur": 52.0,
 "bpm": 110,
 "vo": {
  "L01": 0.15,
  "L02": 6.8,
  "L03": 14.5,
  "L04": 28.0,
  "L05": 42.0
 },
 "hook": {
  "t0": 0.12,
  "t1": 5.2,
  "metric": "$0",
  "text": "The $0 garden fix that out-performs commercial root stimulator."
 },
 "caps": [
  {
   "t0": 5.4,
   "t1": 8.6,
   "en": "Garden centers charge $18|for rooting hormones.|{Most are 99% talc}."
  },
  {
   "t0": 8.8,
   "t1": 13.5,
   "en": "Penn State tested willow water|against chemical powder.|{The willow won by 42%}."
  },
  {
   "t0": 13.8,
   "t1": 18.2,
   "en": "Here is the 10-second recipe|using branches|{already in your yard}."
  }
 ]
}
```

---

## 6. Project & File Locations

- **Style Assets & Engine**: `D:\0002-Team A Nam\styles\caption-news\`
- **Style Documentation**: [styles/caption-news/STYLE.md](file:///D:/0002-Team%20A%20Nam/styles/caption-news/STYLE.md)
- **Metadata**: [styles/caption-news/style.json](file:///D:/0002-Team%20A%20Nam/styles/caption-news/style.json)
- **Engine Runner**: `C:\Users\admin\lemo-opuscar\` (Core Playwright & Audio tools).
