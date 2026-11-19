#!/bin/bash
# Copy to reels/edit/<w>-scenes.sh and fill in. Run with WEBINAR_SHORTS_ENV=<skill dir>/scripts/env.sh.
# Scenes are animated popups in the field above the speaker's window (box 60,240,900,340), in the MobiDev Brand Book
# 2026 look (assets/brand-mobidev/rules.md): #222222 / #FFFFFF plates, green #4AD57B for the answer or the gain,
# coral #DE7356 only for a problem (the strike in `contrast`). Tone `feature`: cards slide in 60 px and land on the word.
#
# MOTION RHYTHM (per video): 3–5 scenes, so a popup lands at least every 8–10 s after the hook goes away.
#   - the first scene starts within 1–2 s after the hook leaves (render.sh keeps the hook until the first scene);
#   - mix types, never the same type twice in a row: list → stat → contrast → quote, word (timeline/funnel/grid-pick);
#   - a scene lasts the time its words are spoken plus the hold (validate tells you if it is too short);
#   - leave ≥ 0.6 s of calm between two popups; nothing in the last 2 s before the end card.
# Which popup for which line of speech:
#   list      "three things / first… second…"            items pop in one by one, each on its own word
#   stat      any spoken number, %, x-times, hours       counter runs up (H1 Inter Black), caption below
#   contrast  "not X but Y", "instead of", "used to"      X struck through in coral, Y lands on a green plate
#   word      steps/stages (timeline), narrowing (funnel), "out of 200 we picked 5" (grid-pick)
#   quote     the single strongest sentence (verbatim)   tone cinematic, label = the speaker's NAME only
#   hook      (rendered by render.sh from <w>-hooks.tsv; don't add one here)
# Texts come from the speech: quote lines must be a verbatim run of transcript words; list items, captions and contrast
# halves may be paraphrased; numbers only as spoken.
# Anchors: --at "word:<word>#<n>" (n-th occurrence in the rough cut; check with words.py out <id>).
# Then: python3 $S/visual_plan.py validate edit/<id> --card  → 0 errors (extend --dur / move --at until it passes).
source "${WEBINAR_SHORTS_ENV:?set WEBINAR_SHORTS_ENV=<skill dir>/scripts/env.sh}"
VP="python3 $S/visual_plan.py"
add(){ id=$1; shift; (cd "$REELS" && $VP add edit/$id --kind scene --mode overlay --box 60,240,900,340 --source speech \
  --tone feature --transition slide "$@") || echo "!! add failed: $id $*"; }
# a quote: same, scale-in instead of a slide
addq(){ id=$1; shift; (cd "$REELS" && $VP add edit/$id --kind scene --mode overlay --box 60,240,900,340 --source speech \
  --tone cinematic --transition fade "$@") || echo "!! add failed: $id $*"; }

# --- one video, four popups (≈ 45 s) ---------------------------------------------------------------------------
# add w14-01 --type list --at "word:show#1" --dur 12.0 --source-ref "09:26-09:45" --lines "Real AI SDLC shows up as" \
#   --items-json '[{"text":"A written spec first","at":"word:spec#1"},{"text":"Context files in the repo","at":"word:context#1"},{"text":"Reviews by people","at":"word:review#1"}]' \
#   --what "signs of a real AI SDLC" --why "readable without sound"
# add w14-01 --type stat --at "word:speed#1" --dur 4.5 --source-ref "26:24-26:28" \
#   --value-json '{"from":0,"to":40,"prefix":"+","suffix":"%"}' --lines "code writing speed" --what "+40%" --why "the key number"
# add w14-01 --type contrast --at "word:prompt#2" --dur 4.0 --source-ref "27:02-27:06" \
#   --lines "Prompting" "Engineering the context" --what "the shift" --why "the before/after of the talk"
# addq w14-01 --type quote --at "word:definition#1" --dur 6.5 --source-ref "06:36-06:44" \
#   --lines "AI is in every stage of the cycle," "not just in the IDE" --accent "every stage" --label "SERHII IVANOV" \
#   --what "the definition as a quote" --why "the video's main thought"
#
# --- word scenes (diagrams that build on the speech) -----------------------------------------------------------
# add w14-02 --type word --variant timeline --at "word:discovery#1" --dur 9.0 --source-ref "14:10-14:22" \
#   --lines "From idea to release" \
#   --items-json '[{"text":"Discovery","at":"word:discovery#1"},{"text":"Spec","at":"word:spec#1"},{"text":"Build","at":"word:build#1"},{"text":"Review","at":"word:review#1"}]' \
#   --what "the stages" --why "a process becomes a picture"
# add w14-03 --type word --variant grid-pick --at "word:hundred#1" --dur 5.0 --source-ref "31:40-31:46" \
#   --value-json '{"to":3}' --lines "200 ideas → 3 shipped" --what "the selection" --why "the number made visual"
