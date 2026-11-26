# Independent Script Audit — ROUND 2 (v2, post-fix verification)

> Auditor: independent pass, no memory of the writer's session. Verifies whether Round-1 fixes actually
> landed, and whether the fixes themselves introduced new problems.
> Script: `script.md` · Outline: `outline.md` · Research: `research-brief.md` · Spine: `retention-spine.md`

---

## 1) HEADER

```
MODE: A (Standard, with YMYL chemical-safety subsection) | DATA: DATA MODE | LANGUAGE: EN | VIDEO TYPE: Standard
DNA VOICE:          Moderate  (up from Weak — 2 of 3 flagged gaps closed, 1 undershoots its own target)
NARRATOR INTEGRITY: Pass (0 flags)
HOOK:               Pass
COMPLIANCE (flag):  Clean (0 blacklist hits; YMYL chemical disclaimer adequate per research-brief bar)
=> VERDICT: REVISE (light) — no structural rewrite needed; 3 small, mechanical polish items
```

Word count: **1,357–1,388 words** (paragraph-split tool gave slightly different counts depending on
tokenization) — inside the 1,200–1,500 target. Estimated runtime at the channel's own 150 wpm / 2.5 wps
benchmark (`video_length._why` in channel.config.json): **~9:15**, inside the 8–10 min target. The v2
texture additions ("Picture this," consensus wrapper, "don't panic" + disposal, signposting) did **not**
blow the word budget — this is a genuine pass, not just a lucky number.

---

## 2) DID THE ROUND-1 FIXES ACTUALLY WORK?

| Round-1 fix claimed | Verified? | Notes |
|---|---|---|
| Hook opens with "Picture this:" | ✅ Works | Satisfies CR1 (sensory + second-person + imperative first word); mechanism proof ("the nitrogen trap") lands at ~16s, well inside L6's <20s window. |
| Consensus-synthesis wrapper around the 2 back-to-back citations | ✅ Works | Both citation pairs (J. Exp. Botany + PNAS in para 6; EPA + NLM in para 15) are now bracketed by folksy setup/payoff lines ("researchers don't even agree… Different paths, same dead end…" / "don't panic… here's the simple, safe way…"). Blend Rule's letter (no 2 sentences literally opening "Research shows…") and spirit are both satisfied. |
| Idiom + folksy marker + social proof added | ✅ Works | Idioms: "green thumb reflex," "dirt-cheap" (≥2 ✓). Folksy marker: "Master gardeners hear this complaint from **folks** constantly" (✓). Social proof: same sentence, anonymous ("Master gardeners… folks") (✓). |
| Contractions 45%→58% | ⚠️ **Undershoots its own target** | Independently recounted at **58.4%** of sentences (52/89) — same number the writer reported, but the brand-voice floor is **≥60%** (`brand-voice-dna.md` Tier 1). The fix moved the needle but stopped just short of the bar it was aiming for. Fixable with 1–2 sentence-level contractions, not a rewrite (see §7). |
| Accessibility Anchor added | ❌ **Not actually present** | `channel-truth.md` defines this element narrowly: short ease-signaling clauses like *"Just 1 drop," "Takes 30 seconds," "No tools needed."* Scanning the full script, this pattern does not appear. The closest candidates ("just less nitrogen," "that's it — that's the whole fix") are simplicity *summaries*, not ease/effort-reduction anchors. Required frequency is ×2–3/script; current count is effectively 0. This is a real, unresolved gap — the task description says it was added, but it isn't there in the form the brand file specifies. |
| "Don't panic" wrapper + disposal guidance for potassium permanganate | ✅ Works, and improved YMYL coverage meaningfully | "Don't panic if you've already got some under the sink" lands naturally, matches signature frequency (×1/script per DNA file), and doesn't undercut the safety message. Disposal line ("your local household hazardous-waste facility will take it off your hands") is generic, defensible civic advice — doesn't need a citation, isn't a science claim, and closes a real gap (a viewer reading this has an actual next step for the bottle under their sink). |
| Signposting "twist one closed, twist two's about to get a lot more literal" | ✅ Works, best fix of the round | This single line does three jobs at once: (a) it's the mid-video re-hook required at the MIDROLL_DIP_ZONE (lands ~5:09, inside phút 4–6), (b) it explicitly subordinates the phosphorus-myth reveal to the permanganate warning, giving the script one clear climax instead of two competing ones (Cinematic Toolkit rule 8), and (c) it's genuinely quotable/memorable for a senior TTS audience. No new problems introduced. |

**Net verdict on the round-1 fixes:** 5 of 7 landed cleanly, 1 (contractions) landed just short of its own
stated target, 1 (accessibility anchors) did not land at all despite being reported as done. Neither gap is
severe — both are small, mechanical additions, not restructuring.

---

## 3) DID ANY FIX CREATE A NEW PROBLEM? (the specific question this round was asked to check)

- **Did the texture pass dilute the science?** No. Re-read against `research-brief.md`'s Verified Claims
  Table — every claim in the script (nitrogen/GA-DELLA-SMZ-SNZ mechanism, PNAS FBH4 finding, NDSU
  phosphorus-myth, Purdue/Nebraska pH-7.0 lockout, EPA non-registration, NIH/PMC case reports) still maps
  cleanly to a Verdict ✅ row. The folksy wrapping sits *around* the citations, not inside them — the
  hedges ("not to zero," "generally doesn't boost," "no simple antidote") are preserved intact.
- **Did "don't panic" read as glib given the real injury risk?** No — it's immediately followed by "here's
  the honest, no-drama version of what you need to know," which reframes it as tone-setting, not
  minimizing. The actual hazard language (corrosive, burns, no antidote, keep from kids/pets) stays fully
  intact after the reassurance line.
- **Did the added signposting line push the Ultimate Payoff beat past its Spine budget?** Marginally.
  Spine target for "5:30–7:00 Ultimate Payoff" is a ~90s window; actual content (wood ash + permanganate,
  now carrying the disposal-guidance addition) runs ~5:19–7:11, about **11 seconds over** the planned exit
  point. Not enough to threaten the 8–10 min ceiling on its own (final runtime is still ~9:15), but it's the
  first thing to trim if the video needs to shorten later — see §7.
- **Did the para-4 "old-timers" insertion (used to plant the folksy marker) create redundancy?** Yes — see
  Retention Leak #1 below. This is the one place a v2 addition measurably cost something instead of being
  free.

---

## 4) TOP 3 RETENTION LEAKS (none are severe; all are concrete and quotable)

**1. 🟡 Redundant restatement right after Status Quo (v2-introduced, ~1:54–2:06)**
> *"...that instinct is exactly backwards."* (end of para 3) → *"You'll hear old-timers say it all the
> time: 'if it's not blooming, feed it more.' Turns out, for this one plant, that well-meaning advice is
> exactly what keeps the trap locked shut."* (para 4)

These two sentences make the identical point twice in a row — "the common instinct is wrong" — right before
the mechanism explanation starts. It reads as filler on a re-listen, and it's the one place the texture
fix (adding the "old-timers" folksy line) measurably cost something instead of being free. **Fix:** cut the
first clause of para 4 and fold the "old-timers" idiom directly onto the existing backwards-instinct line,
e.g.: *"For this one plant, that instinct is exactly backwards — and it's the same 'feed it more' advice
you'll hear from old-timers at the nursery counter."* Saves ~15 words, keeps the folksy marker.

**2. 🟡 Ultimate Payoff block is the single densest paragraph in the script (190 words / ~76s, para 15)**
> *"The second one's the one to really watch: potassium permanganate... [continues for 190 words]"*

It has good internal sub-beats (name → reassure → evidence → evidence → action → relief), so it isn't a
flat wall of citations, but at ~76 seconds of continuous prose it's more than double the length of any
other beat in the script, sitting right at the tail of MIDROLL_DIP_ZONE (phút 4–6) where L5 asks for
tension/payoff every 60–90s. **Fix:** break after "...with no simple antidote" — insert a one-line
pattern-break ("So no, you don't need to panic about the bottle under the sink. You do need a plan for
it.") before pivoting into the handling/disposal steps. Keeps every fact, adds one more beat.

**3. 🟡 Accessibility Anchor still missing (ties to retention, not just voice checklist)**
Seniors are the explicit audience (`target_viewer` in channel.config.json), and the channel's own signature
list requires 2–3 short "this is easy" reassurance beats. Two natural insertion points: right after the
soil-test recommendation (para 10) and right after the "less nitrogen" fix reveal (para 9). **Fix examples:**
*"Takes about a minute to write down what your soil test says."* / *"Just one number to watch on the bag —
that's it."* This isn't purely cosmetic: for a 60–80-year-old audience, an explicit "this won't be hard"
beat is a documented engagement lever for this channel, not decoration.

---

## 5) HOOK CHECK — HOOK_DROPOFF_ZONE (giây 40–55)

- [x] Pain/contrast opener: "thick, green, and absolutely gorgeous — and it hasn't given you a single flower."
- [x] Open loop: "half of what most gardeners try to fix it with is actually a myth."
- [x] First words: "Picture this:" — imperative, sanctioned by CR1.
- [x] Mini-payoff <20s: "Researchers have a name for this: the nitrogen trap" lands ~16s.
- [x] **HOOK_DROPOFF_ZONE content check:** at 40–55s the script is mid-sentence naming potassium
  permanganate as the more dangerous of the two soil "fixes" — this is substantive content, not a
  "preview/intro" pivot, so L4 is satisfied.

**One low-confidence note, not a flag:** naming *which* chemical is dangerous this early (40–50s) closes
part of Loop #2 well before the Spine's planned payoff at 5:30–7:00. It didn't cost retention in this
review (the *why* is still withheld, so curiosity should hold), but it's worth knowing this was a deliberate
early reveal, not an oversight, if a future round wants to test holding the name back.

**Verdict: PASS.**

---

## 6) DNA VOICE AUDIT

- **Signature elements present:** "Here's why this works" + analogy (light-switch, teenager growth-spurt)
  ✓ · exact numbers (5-10-10, EPA, pH 7.0, twenty-eighteen study) ✓ · 3 mistakes (explicit, each
  differentiated) ✓ · anonymous social proof ("Master gardeners… folks") ✓ · neighbor payoff scenario
  ("Meanwhile the neighbor's… stays all leaves") ✓ · `Happy gardening.` ✓
- **Signature elements missing/weak:**
  - **Grandmother-or-personal-failure story** — absent. "Old-timers say it all the time" partially covers
    the folk-wisdom function but isn't the literal required beat, and nostalgia is the channel's
    #1-engagement comment theme (`channel-stats` Theme 1) — this is a real missed lever, not just a
    checklist gap. Low-cost fix: reframe the old-timers line as "A gardener I spoke with put it this way…"
    (still narrator-safe, still anonymous).
  - **Accessibility Anchors ×2-3** — see Retention Leak #3 above.
  - **Cost comparison (DIY vs store)** — soft ("save that money," "dirt-cheap") but never lands an actual
    $ figure. Not required to be a hard number, but CR6 (cost transparency + value-ratio anchor) asks for
    something more concrete than a phrase. Optional upgrade, not a gate item.
- **Human Texture E7:** contractions 58.4% (target ≥60%, see §2) · idioms 2/2 (green thumb, dirt-cheap) ✓
  · folksy marker 1/1 (folks) ✓ · 0 AI-cliché matches (delve/leverage/utilize/etc. — none found) ✓.
- **Sign-off:** present and does something extra — "throw the party it's been waiting for" calls back to
  the earlier metaphor ("keeps building more house instead of throwing the party," para 6), giving the
  mantra closure an actual payoff instead of a generic wrap-up. Worth preserving as-is.

**Verdict: Moderate** (up from Weak). Not "Strong" only because of the two items above — both are small,
mechanical additions, not a voice problem.

---

## 7) NARRATOR INTEGRITY SCAN

No violations found. Full fake-experience blacklist swept (I've grown/tested/planted, my garden, when I
was, I remember, for X years, after decades, my experience, I personally) — zero matches. All authority is
attributed to institutions (EPA, NIH/PMC, Purdue, Nebraska Extension, NDSU, named journals), never to an
unsourced personal name, consistent with `brand-voice-dna.md` Social Proof rules. Script correctly does
**not** use the unverified Clematis 'Jackmanii' history lead flagged in `research-brief.md`'s Story Bank
("trống" — no verified source) — good restraint, avoids a fake-witness flag.

**Verdict: Pass, 0 flags.**

---

## 8) STORYTELLING CRAFT CHECK

- **Transitions:** mostly bridged, not "trạm dừng." The para 12→13 transition ("That's twist one, closed.
  Twist two's about to get a lot more literal.") is the standout — explicit close + contrast + tease in one
  line.
- **Scene:** 1 clear viewer-POV scene (the hook). Toolkit wants ≥1–2; the teenager/growth-spurt-food bit is
  a strong analogy but is written in third person, not viewer-POV, so it doesn't strictly qualify as a
  second "scene." Not a flag — research-brief's Story Bank was empty, so there was no verified second scene
  available to use, and the script correctly didn't fabricate one.
- **Mid-video re-hook at MIDROLL_DIP (phút 4–6):** present and effective (the "twist one closed…" line, see
  above).
- **Climax beat:** correctly singular. The signposting line explicitly subordinates the phosphorus-myth
  reveal to the permanganate warning — one designated apex, not two competing ones.
- **Forward-visual close before Identity CTA:** present ("that same thick green vine could be the one
  covered in blooms by next season... Meanwhile the neighbor's... stays all leaves") followed by "If you'd
  rather understand the 'why'... you belong here." Correct order per Toolkit rule 9.
- **Next-video loop:** absent — correctly so, per Toolkit rule 6 ("KHÔNG hứa nếu chưa có kế hoạch thật").

---

## 9) COMPLIANCE FLAG

- Blacklist absolutes (guaranteed/100%/miracle/cure/detox/heal): 0 matches.
- YMYL (potassium permanganate): disclaimer present and matches research-brief's own recommended framing
  exactly — not registered for garden/soil use (EPA), corrosive with real case reports and no antidote
  (NIH/PMC), no consumer dosing guide. Script correctly avoids the unverified "kills soil microbes" claim
  that research-brief explicitly said not to use.
- Pet/kid safety: present as one clear beat ("well out of reach of kids and pets... even a small amount can
  burn skin or cause real harm if swallowed"), not buried — matches CR5.

**Verdict: Clean.** (Run `mkt-yt-compliance` for the official Monetization Risk Score before export — this
audit only flags, doesn't score.)

---

## 10) LESSONS-LEARNED CHECK (ACTIVE RULES)

| Rule | Status |
|---|---|
| L1 (no exotic/niche plant) | ✅ Clematis is common in US home gardens |
| L2 (specific outcome for counter-intuitive claim) | ✅ "covered in blooms by next season" — best-available given research-brief's NEED DATA on exact timing |
| L3 (deliver title promise in 60s) | ✅ Delivered by ~20s, well ahead of the 60s bar |
| L4 (open loop through giây 40–55) | ✅ Confirmed by word-position mapping — permanganate name-drop lands exactly in this window |
| L5 (tension layer every 60–90s at phút 4–6) | ✅ Signposting line lands at ~5:09, inside the zone |
| L6 (evidence for counter-intuitive claim before giây 20–33) | ✅ "the nitrogen trap" name-drop at ~16s |
| L7 (≤10 min unless Spine earns it) | ✅ ~9:15 |
| L8 (ergonomic pain-stack title) | N/A — different title pattern (Problem-Fix myth-bust), not required for every video |
| CR1–CR11 (competitor-teardown craft rules) | No violations found; CR6 (cost transparency) is the weakest of the set — soft, not absent |
| X1–X5 (avoid-list: conspiracy, absolutes, health-fear, oversimplified-advice-with-consequences, self-experience persona) | 0 matches |

---

## 11) ANTI-SLOP / DIFFERENTIATION CHECK

- ✅ Specific cited numbers/sources inline (EPA, NIH/PMC, Purdue 2026, Nebraska 2019, NDSU 2023, PNAS 2021,
  J. Exp. Botany 2018).
- ✅ ≥2 Consensus Synthesis sentences: "Different paths, same dead end..." (para 6, synthesizing 2
  disagreeing mechanism studies into 1 takeaway) and "Purdue and Nebraska Extension research agree on this"
  (para 14, classic 2-source convergence).
- ✅ Science → Action → Benefit present (mechanism → "less nitrogen" fix → neighbor payoff).
- ✅ Claim-scoping honest throughout ("not to zero," "generally doesn't boost... when the soil already has
  enough," "don't panic").
- ✅ Differentiated mechanism angle (GA-DELLA-SMZ/SNZ simplified, NDSU phosphorus-myth, pH-7.0 lockout) —
  not swappable with a generic AI-voice garden channel script.
- ✅ No slop patterns (no fake mechanisms, no "stick X inside Y" gimmicks, no unearned absolutes).

**Verdict: Pass**, comfortably clears the ≥2-evidence bar.

---

## 12) ACTIONABLE FIXES (ranked by impact)

1. **[Highest, cheap]** Add 2 short Accessibility Anchor lines (after para 9 "less nitrogen" reveal, and
   after para 10 soil-test mention) — closes a real signature gap, genuinely useful for a 60–80 audience.
2. **[Cheap]** Fix the para 3→4 redundancy (Retention Leak #1) — fold the "old-timers" idiom onto the
   existing "instinct is exactly backwards" line instead of restating it in a new sentence.
3. **[Cheap]** Nudge contractions from 58.4%→≥60% — 1–2 sentence-level edits are enough (89 sentences, 52
   contracted; need ~54 to clear 60%). Candidates: "That tells you what your soil actually has" →
   "That'll tell you..."; "Feeding stops the moment buds start forming" → "Feeding just stops the moment
   buds start forming" (or similar — pick whichever reads most natural aloud).
4. **[Optional]** Insert one pattern-break line inside the 190-word permanganate paragraph (Retention Leak
   #2) to keep the tail of MIDROLL_DIP_ZONE from running as one continuous 76s block.
5. **[Optional, upgrade not gate]** Turn the soft "save that money" cost mention into 1 concrete $ anchor
   if a real number exists (e.g., typical price of a "bloom booster" bag vs a standard low-N fertilizer) —
   only do this if the number can be sourced; don't invent one.

None of these require touching the structure, the science, or the climax placement — all five are
sentence-level edits.

---

## 13) INLINE TAGS REPORT

`[PET-SAFETY]` present, 1 beat, not buried (para 15).
`[COMPLIANCE]` 0 flags.
`[YMYL]` handled per research-brief's own recommended framing (chemical safety, not "kills soil microbes").
`[NEED DATA]` — none leaked into the final script text (all research-brief NEED DATA items were correctly
converted into honest hedges, e.g. "in the vòng 1 mùa sinh trưởng" → "by next season," not a fabricated
week-count).
`[HEDGE]` — present and accurate throughout (see §11 claim-scoping).

---

## VERDICT GATE

**REVISE (light).** DNA Voice is Moderate, not Strong, due to two small, mechanical gaps (Accessibility
Anchors, contractions at 58.4% vs ≥60% floor) plus one v2-introduced redundancy (Retention Leak #1).
Narrator Integrity, Hook, Compliance, and Lessons-Learned all pass cleanly. None of round 1's original
findings (weak hook, back-to-back citations, missing disposal guidance, unsignposted climax) survived — all
5 of those fixes verified as genuinely resolved. This round's open items are all sentence-level, not
structural — a light pass should be enough to reach PUBLISH.

**Reminder:** enable "Altered or synthetic content" on upload (AI Voice). Producer sign-off before VoiceAI
export.
