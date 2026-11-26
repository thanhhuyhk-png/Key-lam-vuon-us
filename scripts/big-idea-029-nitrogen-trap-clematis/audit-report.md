# Audit Report — Why Your Lush Green Clematis Never Blooms (1 Fertilizer Mistake)

> Independent QA — mkt-youtube-script-audit | Date: 2026-07-14
> Word count verified: **1,360 words** (target 1,200–1,500 ✅) ≈ 9:00 @ ~151 wpm (matches video_length 8-10' config)

---

## 1) HEADER

```
MODE: C (YMYL — corrosive-chemical safety content: potassium permanganate) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Problem-Fix / Myth-bust + chemical safety
DNA VOICE:          Weak
NARRATOR INTEGRITY: Pass (0 flags — clean scan, zero hands-on claims)
HOOK:               Needs work
COMPLIANCE (flag):  1 flag (missing disposal guidance for corrosive chemical) → run mkt-yt-compliance for official Risk Score
=> VERDICT: REVISE
```

DATA MODE confirmed via `channel-stats-garden-us-60k.md` (AUDIT TL;DR block): `BASELINE_AVD=25.6%`, `HOOK_DROPOFF_ZONE=40-55s`, `MIDROLL_DIP_ZONE=phút 4-6`. Reclassified MODE A→**C**: the script gives storage/handling instructions for a corrosive chemical with real NIH-documented burn/poisoning case reports — this crosses into YMYL chemical-safety territory even though the outline tagged it "Standard."

---

## 2) TOP 3 RETENTION LEAKS

**Leak #1 — DNA Voice collapses right where the video needs warmth most (throughout, worst in the 4-6min payoff zone)**
> **[trích]** *"Case reports published through the National Library of Medicine describe real burns and poisoning from skin contact or accidental swallowing, with no simple antidote... Gloves on every time you handle it, and never guess at a dilution."*
→ **Lý do rớt:** This reads like an extension bulletin, not "lazy grandma wisdom." Full-script scan: **0 gardener idioms** (need ≥2), **0 folksy markers** (need ≥1), **0 discourse fillers** ("you know"/"I mean" — need rải đều), **0 accessibility anchors** ("Just 1 drop" style), **0 anonymous social proof** ("a viewer in Ohio"), **0 grandmother/failure story**, contractions only **45%** of sentences (target ≥60%). This is exactly the payoff zone (phút 4-6, MIDROLL_DIP) where the channel's own data says viewers are already leaving — a cold, clinical tone here compounds the risk instead of anchoring trust.
→ **Bản vá (giữ DNA Voice):** Wrap the safety fact in a Stance Phrase before delivering it: *"Now, here's the thing — you don't need to panic about this one. If you've already got some under the sink, here's the simple, no-drama way to keep everyone safe: keep it in a tightly sealed container, well out of reach of kids and pets — gloves on if you ever handle it, and never guess at a dilution."* Adds "Here's the thing" (signature phrase) + "don't panic" (required stance) + softens the clinical NIH-citation delivery without diluting the safety content.

**Leak #2 — Two research citations stacked back-to-back right before the dip zone (≈2:14–3:34)**
> **[trích]** *"A twenty-eighteen study in the Journal of Experimental Botany traced it to a hormone pathway that gets suppressed when nitrogen is high. A separate study published in the Proceedings of the National Academy of Sciences found nitrogen changes a different protein that also controls flowering timing."*
→ **Lý do rớt:** Two consecutive citation-led sentences violate the Blend Rule in `brand-voice-dna.md` ("Max 1 cụm research-authority / science moment; KHÔNG mở 2 câu liên tiếp bằng 'Research shows…'"). For a 60-80yo mobile audience, two journal names in a row right before the video enters the known dip zone is a real mini-leak risk — dense academic language stacked with zero folksy buffer.
→ **Bản vá:** Fold the second citation into a Consensus Synthesis sentence instead of a second standalone citation: *"Now here's the interesting part — the researchers don't even agree on which switch it flips first. One 2018 study traced it to a hormone pathway that shuts off when nitrogen's high. Another, published a few years later, found a completely different protein doing the same job. Different paths, same dead end: too much nitrogen, and the plant just keeps building more house instead of throwing the party."* (already close to what P6 does later — pull that folksy wrapper earlier so it brackets *both* citations, not just the summary line.)

**Leak #3 — Zero scenes in the whole script (Cinematic Toolkit requires ≥1-2)**
> **[trích]** *"Now, for almost every plant you grow, lush green growth really is a good sign."* (Status Quo section, ~1:02)
→ **Lý do rớt:** Story Bank was empty (research-brief confirms) so no documented-history scene was possible — correct call to avoid fabricating one. But a **viewer-POV scene needs no sourcing** and none was used anywhere. The entire script is pure exposition; for a channel whose retention thesis is "brain remembers pictures, not information," this is a missed lever, especially right at Status Quo where a sensory scene would cost nothing and reinforce the pain before the paradigm shift.
→ **Bản vá:** Open Status Quo with a viewer-POV scene instead of general exposition: *"Picture it: every spring you're out there with the fertilizer bag, the vine gets thicker, greener, taller up the trellis — and every June you're still standing there counting zero blooms."* Then continue into the existing "for almost every plant you grow..." line.

---

## 3) HOOK CHECK — soi đặc biệt HOOK_DROPOFF_ZONE (giây 40-55)

- [x] Đòn đau / viễn cảnh tương phản — "thick, green, gorgeous — hasn't given you a single flower"
- [x] Open Loop — "half of what most gardeners try to fix it with is actually a myth" (Loop#1) + potassium permanganate tease (Loop#2)
- [ ] **5 từ đầu mạnh (verb mệnh lệnh / pain statement)** — FAIL. First 5 words: *"Your clematis is thick, green"* — descriptive, not imperative/pain-forward. Compare to the channel's own proven patterns (Contradiction / Dramatic-result / Visual command in `brand-voice-dna.md`).
- [x] Mini-payoff trước ~20s — "Researchers have a name for this: the nitrogen trap" lands at word ~27 (well under giây-20 threshold, satisfies L6)
- [x] **[DATA MODE]** HOOK_DROPOFF_ZONE (giây 40-55 ≈ word 100-138): open loop present — "quick heads-up, that one is potassium permanganate... isn't safe around kids or pets" — keeps tension instead of sliding into flat preview. PASS.

**Fail on first-5-words → 2 rewrite variants (giữ DNA Voice, giữ đúng claim đã verify):**

1. *"Stop feeding that clematis — the greener it gets, the further away those flowers might be."*
2. *"Picture this: your clematis is thick, green, gorgeous — and it hasn't given you a single flower."* (adds the missing viewer-POV scene from Leak #3 at the same time)

---

## 4) DNA VOICE AUDIT

Chấm theo `channel-truth.md` TL;DR + `brand-voice-dna.md`:

| Signature element (bắt buộc) | Có/thiếu |
|---|---|
| Grandmother-or-failure story | ❌ Missing — only "old-timers say it all the time" (1x), no grandmother framing at all |
| "Here's why this works" + analogy | 🟡 Partial — "Here's what's actually happening inside the plant" + teenager analogy (good), but exact signature phrase "Here's why this works" never appears |
| Exact numbers | ✅ Strong — 2018 study, PNAS, NDSU 2023, pH 7, 20-20-20, 5-10-10 |
| 3 mistakes | ✅ Present, clean (P16) |
| Cost comparison (DIY vs store) | ❌ Missing — only "you can save that money," no $ figures |
| Anonymous social proof ("a viewer in Ohio") | ❌ Missing entirely — 0 instances |
| Accessibility Anchors ×2-3 | ❌ Missing — 0 instances of the "Just 1 drop" pattern (11 uses of "just" found, none in anchor format) |
| Sign-off "Happy gardening." | ✅ Present |

**Human Texture E7 — FAIL on 3/4 sub-checks:**
- Contractions: **45%** of sentences (target ≥60%) 🔴
- Gardener idioms (rain or shine / green thumb / dirt-cheap / proof is in the pudding…): **0** (target ≥2) 🔴
- Folksy markers (folks / trust me / give it a whirl): **0** (target ≥1) 🔴
- AI clichés blacklist: **0 matches** ✅ clean

**Signature phrases frequency check:** "Here's the thing" ×1 (target present) ✅ · "Here's why" ×0 (target 2-3) ❌ · "Don't panic" ×0 (target 1) ❌ · "That's it" ×0 (target 1) ❌ · "Non-negotiable" ×0 (not required but a known signature) — absent.

**Diagnosis:** the script nails the "Science-Backed Proof" half of the voice formula (citations, hedging, mechanism accuracy are excellent) but has almost entirely dropped the "Lazy Grandma Wisdom" half. This reads like the writer spent the compliance/accuracy budget on the double-myth-bust and safety hedging (reasonably, given how tricky that content is) and never circled back to re-inject texture. → **DNA VOICE = Weak**, fixable with a texture pass — does not require re-writing content, just re-clothing existing sentences.

---

## 4.5) STORYTELLING CRAFT CHECK

- [x] **Transitions** — no bare "trạm dừng." Every section change uses a contrast/callback bridge ("Now, remember that twist from earlier?", "And speaking of things gardeners reach for that don't do what they promise", "The second one is the one to really watch"). Good craft.
- [ ] **Scenes** — **0/script** (need ≥1-2). Story Bank was empty so no documented-history scene was possible (correct restraint), but a viewer-POV scene (no sourcing required) was never used. See Leak #3.
- [x] **Mid-video re-hook at MIDROLL_DIP (phút 4-6)** — present and well-executed: the myth-bust payoff ("What actually works about a fertilizer like five-ten-ten isn't the phosphorus at all — it's the lower nitrogen number") lands at word 616-724 ≈ **4:05-4:47**, squarely inside the spine's designated 600-850 word-index target and the channel's real MIDROLL_DIP_ZONE.
- [ ] **Climax Beat — designated vs. competing.** ⚠️ **This is the answer to your specific question.** The Retention Spine correctly *places* the phosphorus-myth reveal at the top of the dip zone (word ~616-724). But it does **not stay the tallest peak**: the potassium-permanganate paragraph that follows (word 885-1041, ≈5:52-6:53) is the **longest paragraph in the script (156 words)** and carries the most viscerally dramatic content — corrosive chemical, real burns, no antidote, EPA non-registration. Structurally this reads as a **second, undesignated climax** stacked right after the "official" one, rather than a supporting beat that "serves" it (per Cinematic Toolkit rule 8: "Các item khác phục vụ đỉnh này, không cạnh tranh nó"). Net effect for retention is probably *not* harmful — it keeps tension climbing through the entire dip window rather than dropping after the myth-bust — but it means the "twist kép" is really a **twist triple** (nitrogen mechanism → phosphorus myth → chemical-safety warning), and none of the three is clearly signposted as *the* peak. Recommend a 1-line pattern-break marker right after the myth-bust to explicitly close that loop before opening the next ("That's twist one closed. Twist two is about to get a lot more literal.") so the viewer's mental model doesn't have to guess which reveal was "the" answer.
- [ ] **SSSQ check** — single subject holds (clematis + nitrogen), but the "single question" softens from "why won't it bloom" to a second, related-but-distinct question ("which soil fixes are dangerous") for the back third of the video. This is *announced* in the Hook/Preview (not a bait-and-switch), so it's not a hard violation — but it does mean the video carries **4 distinct payoff threads** (nitrogen mechanism, phosphorus myth, wood-ash pH lockout, permanganate safety) in 9 minutes for a 60-80yo audience. Not a REVISE-blocker on its own, but combined with Leak #2 (citation density) it's the same underlying risk: information load outpacing warmth pacing.
- [x] **Forward-visual close** — present: "that same thick green vine could be the one covered in blooms by next season. Meanwhile the neighbor's — still getting fed like a lawn — stays all leaves." Good neighbor-payoff + forward image.
- [x] **Identity CTA** — "If you'd rather understand the 'why' than just throw more fertilizer at a problem, you belong here." + geo-specific comment question. Good.
- [ ] Closing mantra is a 3-beat variant ("growing smart, feeding less, and finally watching it throw the party") but doesn't match the documented "[verb] + save money + have some fun" template — acceptable creative variation, flagging as minor drift only.

---

## 5) NARRATOR INTEGRITY SCAN

**Clean — 0 violations.** Full-text scan for fake-experience blacklist ("I've grown/tested/spent/planted", "my garden", "my clients", "when I was", "I remember", "for X years", "after decades", "I personally") returned **zero matches**. Only first-person instance in the entire script is "I'd love to hear in the comments" (engagement CTA, not an experience claim). All authority is correctly routed through research-authority phrasing (extension offices, EPA, NIH, PNAS). This is a genuine strength — no fixes needed here.

---

## 6) COMPLIANCE FLAG (light — not official Risk Score)

- Blacklist absolute terms (guaranteed/100%/miracle/cure/detox/heal-as-medical-claim): **0 hits** — clean.
- 🔴 **1 flag — incomplete YMYL safety guidance.** The potassium permanganate section gives storage/handling instructions ("keep it in a tightly sealed container... gloves on") but never tells the viewer what to actually **do** with it long-term — no mention of contacting a local household hazardous-waste facility for disposal, and no "if skin/eye contact occurs, seek medical attention" or Poison Control pointer. Given NIH case reports of real burns/poisoning are cited directly, MODE C expects the disclaimer to close the loop on *what to do*, not just *how to store it safely in the meantime*.
- Pet/Kid safety: present and clear for both wood ash context (implicit) and permanganate ("out of reach of kids and pets"). ✅
→ Recommend running `mkt-yt-compliance` after the texture/safety revisions for the official Risk Score.

---

## 6.5) LESSONS-LEARNED CHECK (ACTIVE RULES + CR1-CR11)

| ID | Result |
|---|---|
| L1 (no exotic plant) | ✅ Pass — clematis is common |
| L2 (counter-intuitive needs concrete outcome) | ✅ Pass |
| L3 (deliver title promise in 60s) | ✅ Pass — "nitrogen trap" named at word ~27 |
| L4 (open loop through 40-55s) | ✅ Pass |
| L5 (tension layer every 60-90s at 4-6min) | ✅ Pass — dense payoff stacking in dip zone |
| L6 (evidence before ~20s) | ✅ Pass |
| L7 (≤10min default) | ✅ Pass — ~9:00 |
| L8 (ergonomic senior stacking) | ➖ N/A for this Problem-Fix angle |
| CR6 (cost transparency + $ anchor) | 🟡 Weak — no concrete $ figures anywhere (soil test cost, bloom-booster price) |
| CR7 (hero anchor) | ✅ Pass — "nitrogen"/"the nitrogen trap" repeated throughout, though not a repeated *number* per Sentence Structure Signature #2 |
| X1-X5 (avoid list) | ✅ Clean — no conspiracy, no absolute claims, no fear-mongering, no oversimplified-harm mechanism, no self-experience claims |

---

## 6.7) ANTI-SLOP / DIFFERENTIATION CHECK

- [x] Specific data + inline citations (2018 J. Exp. Botany, PNAS 2021, NDSU 2023, EPA archive, NIH/PMC) — strong, verifiable, matches research-brief exactly.
- [x] **≥2 Consensus Synthesis sentences** — (1) "Researchers word this differently depending on the study. But they keep landing on the same conclusion" (3 studies → 1 principle); (2) "Purdue and Nebraska Extension research agree on this" (2 sources → 1 principle). Meets the ≥2 bar.
- [x] Science → Action → Benefit — consistently closed (soil test → know what you have; light wood-ash dusting → avoid pH lockout).
- [x] Claim-scoping honest — "not to zero," "generally doesn't boost... when the soil already has enough," "if it's mishandled."
- [x] Mechanism/research angle other channels in this niche won't have (the phosphorus-myth-inside-the-nitrogen-myth twist is genuinely differentiated).
- [x] No slop pattern (no fake mechanisms, no unsourced miracle claims).

**Verdict: PASSES anti-slop bar** — this is the strongest section of the script and the main reason accuracy/authority isn't in question here. The gap is entirely in delivery warmth (Section 4), not substance.

---

## 7) ACTIONABLE FIXES (xếp theo tác động)

1. **[HIGH]** Texture pass on the whole script to hit Human Texture E7: add ≥2 gardener idioms, ≥1 folksy marker, push contractions from 45%→60%+, add 2-3 real Accessibility Anchors. Do this by rewriting sentences in place — no content needs to change.
2. **[HIGH]** Re-wrap the potassium permanganate safety block (Leak #1) with a Stance Phrase ("here's the thing, don't panic...") before/after the clinical NIH citation, and add explicit disposal guidance ("if you're not going to use it, your local household hazardous-waste facility will take it off your hands") to close the YMYL loop (Section 6).
3. **[MED]** Split/soften the back-to-back citation stack at ~2:14-3:34 (Leak #2) with a folksy Consensus-Synthesis wrapper bracketing both studies instead of a flat second citation sentence.
4. **[MED]** Rewrite hook opening to lead with pain/imperative instead of flat description (Section 3, 2 variants provided) — also doubles as the missing viewer-POV scene (Leak #3).
5. **[LOW]** Add 1 explicit anonymous social-proof line ("A viewer in Ohio tried this last spring and finally got blooms by August") and 1 concrete cost anchor ($ for soil test vs $ for bloom-booster fertilizer) to restore 2 more missing signature elements.

---

## 8) INLINE TAGS REPORT

`[NEED DATA]` 0 · `[YMYL]` 1 (potassium permanganate — see Section 6) · `[PET-SAFETY]` present and adequate · `[HEDGE]` adequate throughout (phosphorus myth, wood-ash dosage, timeframe) · `[COMPLIANCE]` 1 (disposal guidance gap)

---

## VERDICT GATE

**REVISE.** Substance, research accuracy, narrator integrity, hook structure, and mid-roll payoff placement are all genuinely strong — this is not a REJECT-tier script. The block is entirely in DNA Voice texture (Weak, fixable without touching content) plus one safety-completeness gap (disposal guidance) and a minor hook-opener tweak. None of these require new research or restructuring — a texture + safety-language revision pass should be enough to move this to PUBLISH.

> Reminder: bật "Altered or synthetic content" khi upload (AI Voice). Producer sign-off TRƯỚC khi VoiceAI export.
