# Audit Report — Why Most Aloe Leaf Cuttings Fail (And What Actually Fixes It)

> Auditor: independent QA (mkt-youtube-script-audit) — no prior context on this script's authoring.
> Script: `scripts/big-idea-036-aloe-cinnamon-propagation/script.md` | Audited against outline.md, research-brief.md, retention-spine.md, channel-truth.md, channel-stats-garden-us-60k.md, lessons-learned.md, brand-voice-dna.md.

---

## 1) HEADER

```
MODE: A (Standard Audit) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard (Problem-Fix / Myth-Correction)
DNA VOICE:          Moderate — voice/tone/consensus-synthesis strong; 2 required signature elements missing
NARRATOR INTEGRITY: Pass — 0 hands-on claims, folklore usage correct, sources narrator-safe
HOOK:               Pass — open loop solid, L6 evidence lands right at the edge of the window (~20.8s)
COMPLIANCE (flag):  Clean — 0 blacklist terms, honest claim-scoping throughout, no fabricated/unverified stats used
=> VERDICT: REVISE
```

**Word count:** ~1,210 words → ~8:04 @150wpm. Within `video_length` target (1200–1500w / 8–10′), at the low end. Retention-spine target was ~1,300–1,350w — script came in leaner, which is fine per L7 but worth noting.

---

## 2) TOP 3 RETENTION LEAKS

**1. [word idx ~110–141, sec ~44–56, inside 🔴 HOOK_DROPOFF_ZONE 40–55s]**
> *"It's one of the oldest tricks passed around in garden circles — even my grandmother swore by it. She wasn't wrong that cinnamon does something. She was just wrong about what."*
→ The retention-spine (Pha B, L4 row) specced a direct re-tease question here ("What's really happening inside the leaf tip?") to keep Loop #1 actively pulling through the drop zone. What shipped is a softer grandmother aside. It technically leaves a loop open ("wrong about what") so it isn't a hard L4 violation, but it's the weakest link in the drop zone — a passive aside instead of an active pull.
→ **Patch (keep grandmother beat, sharpen the loop):** *"It's one of the oldest tricks passed around in garden circles — even my grandmother swore by it. She wasn't wrong that cinnamon does something. She was just wrong about what — and that mix-up is exactly what's about to make sense."*

**2. [word idx ~587–750, sec ~3:55–5:00, approaching 🔴 MIDROLL_DIP_ZONE]**
> *"...Extension experts recommend letting that tip air-dry on the counter for four to seven days... Extension offices land on the same fix: a three-to-two-to-one mix of potting soil, coarse sand, and perlite..."*
→ ~65 seconds of back-to-back procedural instruction (air-dry timing → soil ratio) with no open loop/pattern-break before the re-hook rescues it at ~5:00. Inside tolerance (L5 allows up to 60–90s), but it's the flattest stretch in the script and sits right where the channel's data shows Problem-Fix videos die hardest (-11.3% on the comparable "STOP Pesticides" video).
→ **Patch:** drop a 1-line pattern-break before the soil section, e.g. *"And here's where most people undo everything they just did right — with the wrong dirt."* → then go into the 3:2:1 mix. Gives the stretch a hook instead of two flat facts in a row.

**3. [DNA signature gap — indirectly a retention lever, not a timestamp leak]**
> No anonymous social proof anywhere in the script (`"a viewer in [state]"` / `"one of my subscribers"` — required signature element, and channel-truth's #1 comment-engagement theme is nostalgia/community proof).
→ Missing social proof removes a proven engagement trigger (comment-bait) and a trust anchor for the "6–8 week fair window, and if it doesn't root, no shame" section — that's exactly where a real viewer example would land hardest.
→ **Patch (insert near the "six to eight weeks" beat, ~6:48):** *"A gardener up in Ohio told me hers took almost seven weeks before anything showed — and she almost gave up on it twice. That's normal."*

---

## 3) HOOK CHECK — soi đặc biệt vùng HOOK_DROPOFF_ZONE (giây 40–55)

- [x] Pain/contrast opening: "You dust cinnamon... And most of the time, it still rots." — real failure scenario, second-person.
- [x] Open loop / leading-number anchor: "There's exactly one step most folks skip — and today, I'll show you exactly what it is." — matches L3/spine's "1 bước bị bỏ qua."
- [x] First words: scene-setting second-person ("You dust cinnamon on a dried aloe tip") rather than a command verb — acceptable per CR1 failure-scenario variant, not a violation.
- [x] Mini-payoff before ~20s: counter-intuitive claim stated by word ~30 (~12s): "cinnamon isn't what wakes up new roots."
- [~] L6 evidence in HOOK_DROPOFF_ZONE: Purdue/IBA-NAA evidence block runs word idx 52–86 → **~20.8s–34.4s**. Rule requires evidence before giây 20–33. It lands essentially on the boundary (starts 0.8s after the nominal 20s mark, finishes within the 33s ceiling). Not a hard fail, but zero margin — if TTS pacing runs even slightly slower than 150wpm, this evidence slips past the window entirely.

**Verdict: Pass, tight margin.** No rewrite required, but tightening P1 by ~2 words would buy safety margin (see Actionable Fix #4).

---

## 4) DNA VOICE AUDIT

Checked against `channel-truth.md` §SIGNATURE bắt buộc/script and `brand-voice-dna.md` §AI Quick Start:

| Required element | Status |
|---|---|
| Grandmother-or-failure story | ✅ "even my grandmother swore by it" |
| "Here's why this works" + analogy | ✅ P5 "Here's why this works" + P10 analogy "Think bandage, not growth switch" |
| Exact numbers | ✅ dense throughout (4–7 days, 3:2:1, 3–4 weeks, 6–8 weeks, 1935, IBA) |
| **3 mistakes (structured)** | 🟡 Content present (wet-cut rot / direct sun scorch / watering too soon) but never framed as an explicit "3 mistakes" beat — reads as scattered warnings, not the Content Formula's step-6 structure |
| **Cost comparison (DIY vs store)** | 🔴 Missing — "no money spent on rooting hormone you don't need" has no $ anchor. No dollar figure anywhere in script. This is a bắt buộc element and a proven CR6 lever |
| **Anonymous social proof** | 🔴 Missing entirely — see Leak #3 above |
| Accessibility Anchors ×2-3 | ✅ "Just walking away," "Just a scrap you were about to throw away," "no shovel, no kneeling" |
| ≥60% contractions | ✅ heavy contraction use throughout |
| ≥2 gardener idioms (Tier 2 list) | 🟡 None of the approved idioms (rain or shine / green thumb / Mother Nature's way / from seed to harvest / dirt-cheap / the proof is in the pudding) appear. "Still worth a shot" is colloquial but not on-list |
| ≥1 folksy marker | ✅ "folks" used 3×+ |
| "Happy gardening." sign-off | ✅ present |

**Signature phrase frequency check (brand-voice-dna.md table):**
- "Here's why" → 2 uses (P5, P20) — meets 2–3 target ✅
- "Don't panic" (1× expected) → 🔴 not used
- "That's it" (1× expected) → 🔴 not used ("Simple as that." is a near-miss, not the exact signature)
- "My grandmother" (1–2× expected) → ✅ 1 use
- Accessibility Anchors (2-3× expected) → ✅

**Net: Moderate.** Voice/tone/pacing is genuinely strong (Consensus Synthesis execution is excellent — see §6.7), but 2 bắt buộc signature elements (social proof, cost comparison) are fully absent and 2 signature phrases are missing. This is what pulls DNA Voice from Strong to Moderate — all fixable without a rewrite.

---

## 4.5) STORYTELLING CRAFT CHECK (Cinematic Toolkit, brand-voice-dna.md)

- **Micro-bridges:** mostly present and functional. No hard "trạm dừng" found; transitions like "Now, here's the part that decides whether all of this was worth it" and "this next part is for you" carry momentum well.
- **Scene (≥1):** ✅ 1 documented-history scene ("Back in nineteen thirty-five, researchers at a lab in Yonkers, New York...") — correctly sourced to Story Bank #1 in research-brief.md (Boyce Thompson Institute / IBA discovery), no fabricated names added. Story Bank #2 (Columbus aloe quote) unused — fine, optional.
- **Mid-video re-hook (MIDROLL_DIP 4–6min):** ✅ "Now, here's the part that decides whether all of this was worth it — how do you actually know it's working?" lands at word idx 751 (~5:00) — good placement.
- **Climax beat:** 🟡 Soft-pass. The "watering too soon" mistake + rooting-signs payoff (~5:08–6:24) functions as the emotional/informational peak and sits inside the dip zone with buildup, but it's spread across 3 paragraphs rather than crystallized into one clearly dramatized beat.
- **Forward-Visual Close:** ✅ "In three or four weeks, you could be looking down at the first thin, white root..." — placed correctly right before Identity CTA.
- **Identity CTA:** ✅ "If you're the kind of gardener who'd rather grow it than buy it, you're exactly who this channel's for."
- **Closing mantra (rule-of-three):** ✅ Excellent execution — "giving that tip the time to seal itself, the soil to breathe, and the patience to wait it out" nearly matches the spine's planned mantra verbatim.

---

## 5) NARRATOR INTEGRITY SCAN

**No violations found.** Scanned full fake-experience blacklist (I've grown/tested/spent/planted, my garden, my clients, when I was, I remember, for X years, after decades, my experience, I personally) — zero matches. "Even my grandmother swore by it" is correctly used as folklore, not personal evidence. All source references ("Purdue University's extension service," "a twenty-eighteen study," "researchers at a lab in Yonkers") are narrator-safe and traceable to research-brief.md sources with no invented details.

**Verdict: Pass.**

---

## 6) COMPLIANCE FLAG (light — not an official Risk Score)

- No blacklist absolutes (guaranteed/100%/miracle/cure/detox/heal) — script actively negates overclaim language ("not a miracle one," "not the guaranteed one").
- No YMYL content (propagation technique, not edible/health use) — no disclaimer needed, correctly absent.
- Pet/kid safety: not present. Outline flagged this as optional ("nếu tự nhiên") and this topic (leaf propagation) doesn't carry acute pet risk, so this is not a compliance issue — noted only as a missed engagement lever in Actionable Fixes.

**Verdict: Clean.** Recommend running `mkt-yt-compliance` for the official Risk Score before export, per standard process.

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES)

| Rule | Check | Result |
|---|---|---|
| L1 (no exotic plant) | Aloe — familiar, channel has 6 prior videos | ✅ |
| L2 (counter-intuitive claims need concrete outcome) | "cinnamon isn't a rooting hormone" claim paired with concrete IBA/NAA + numbers | ✅ |
| L3 (deliver title promise in 60s) | "Why most fail" (root rot mechanism) + "what fixes it" (dry/callus premise) both land before word idx 239 (~95s)... actually the core "why it fails" (root rot) lands ~2:24 (word 360) | 🟡 See note below |
| L4 (open loop through 40-55s) | Present but soft — see Leak #1 | 🟡 |
| L5 (tension layer every 60-90s in 4-6min) | Present, within tolerance — see Leak #2 | 🟡 |
| L6 (evidence before sec 20-33 for shock claim) | Evidence lands 20.8-34.4s, boundary-tight | 🟡 |
| L7 (≤10min default) | ~8:04 | ✅ |
| L8 (ergonomic lever for seniors) | "no shovel, no kneeling" present | ✅ |

**Note on L3:** the *mechanism* for "why cuttings fail" (root rot from wet-cutting) is fully explained by word idx 360 (~2:24) — later than the pure hook promise (delivered <20s) but still well within the video's front third, and the outline's own Phần 1/Phần 2 split intentionally sequences "why dried tip has an advantage" (word ~142, ~57s) before "why wet cutting rots" (word ~239-360, ~1:36-2:24). This matches the approved outline structure, not a violation — flagging only because L3 is literally about the *title's* promise ("what actually fixes it"), and the fix itself doesn't fully land until word idx 653 (~4:21, when the soil formula is delivered) and word idx 871 (~5:48, watering guidance). For a Problem-Fix title this is acceptable pacing (the "why" needs to land early, the "fix" can build through the middle), but it's worth knowing the full "fix" doesn't complete until nearly the midpoint.

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

Evidence found (≥2 required — this script has more):
- [x] Specific numbers + inline cite: Purdue (IBA/NAA), 1935 Yonkers/IBA discovery, 2018 succulent-sealing study (~55min/20min), 2020 cinnamon-antifungal study (Botrytis cinerea).
- [x] **Consensus Synthesis — 3 sentences found** (exceeds ≥2 requirement): "Nearly every extension service agrees: cinnamon has real antifungal power, but zero rooting hormone properties" / "Extension offices land on the same fix: a three-to-two-to-one mix..." / "the science is consistent on this: pulling a pup... is the only method researchers treat as standard."
- [x] Science → Action → Benefit: consistently present (e.g., callus mechanism → air-dry 4-7 days → avoids rot).
- [x] Claim-scoping honesty: "It works sometimes, not always," "This is still the backup method, not the guaranteed one."
- [x] Mechanism angle competitors in this niche rarely use: the physical wound-sealing mechanism (55min/20min) and the 1935 IBA origin story are genuinely differentiated, non-generic content.
- [x] No slop patterns detected (no fake mechanisms, no unsourced miracle claims, no interchangeable generic structure).
- **Notable positive:** the script correctly excludes every fabricated/unverifiable statistic flagged in research-brief.md's NEED DATA section (the "Guelph 480 cuttings" stat and "UC Extension >70%" stat) — zero hallucination discipline is excellent here.

**Verdict: Pass, strong.**

---

## 7) ACTIONABLE FIXES (ranked by impact)

1. **[HIGH] Add a $ cost-comparison anchor.** Currently "no money spent on rooting hormone you don't need" has no dollar figure. Insert one specific number (e.g., "skip the $8-10 bottle of rooting hormone" near P2, or "instead of buying a new $15-20 aloe" near P20) — this is a bắt buộc DNA signature element and currently the only missing $-lever in an otherwise numbers-dense script.
2. **[HIGH] Add 1 anonymous social-proof line.** Insert near the "six to eight weeks... no shame in that" beat (~6:48): a viewer/gardener example ("A gardener up in Ohio told me hers took almost seven weeks..."). Zero social proof currently exists; this is a required signature element and the channel's #1 comment-engagement driver per channel-truth.md.
3. **[MEDIUM] Sharpen the 40-55s zone loop.** Add one explicit forward-tease sentence after the grandmother beat to convert the passive "wrong about what" into an active pull line (see Leak #1 patch).
4. **[MEDIUM] Buy safety margin on L6.** Trim 2-4 words from the opening sentence so the Purdue/IBA-NAA evidence clearly lands before the 20s mark instead of right on the boundary (~20.8s currently — zero margin against pacing variance).
5. **[LOW] Restore 1-2 missing signature phrases.** Insert "Don't panic" (fits naturally right before or after the "watering too soon" mistake warning, ~5:20) and/or swap "Simple as that." → "That's it." to hit the exact phrase table in brand-voice-dna.md. Also consider 1 approved Tier-2 idiom (currently 0/2 from the approved list) — low priority, cosmetic.

---

## 8) INLINE TAGS REPORT

- `[NEED DATA]` — none triggered; script correctly avoids every unverified stat flagged in research-brief.md.
- `[YMYL]` — not applicable (non-edible, non-health propagation topic).
- `[PET-SAFETY]` — not present; not required for this topic, noted only as a missed optional engagement lever.
- `[HEDGE]` — appropriately hedged where needed ("four to seven days, give or take"; "3-4 weeks... a few weeks after that").
- `[COMPLIANCE]` — clean, no flags raised.

---

## VERDICT: REVISE

No narrator-integrity, compliance, or YMYL blockers — this is a well-researched, well-sourced script with strong Consensus Synthesis execution and correct hallucination discipline. The REVISE call is driven entirely by two absent bắt buộc DNA signature elements (cost comparison, anonymous social proof) plus a soft spot in the 40-55s drop zone and a boundary-tight L6 timing — all fixable with the 5 targeted patches above, no structural rewrite needed.

---

**Reminders before export:**
- Enable "Altered or synthetic content" on upload (AI Voice).
- Producer sign-off required before VoiceAI export.
- Run `mkt-yt-compliance` for the official Monetization Risk Score before final export.
