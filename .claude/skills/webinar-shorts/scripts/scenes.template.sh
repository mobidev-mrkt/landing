#!/bin/bash
# Copy to reels/edit/<w>-scenes.sh and fill in. Scenes are overlays in the field above the window (box below).
# Texts come from the speech: quote lines must be a verbatim run of transcript words; list items and stat captions
# may be paraphrased, numbers only as spoken. Quote labels: the speaker's NAME only (the label counts toward reading time).
# Anchors: --at "word:<word>#<n>" (n-th occurrence in the rough cut; check with words.py out <id>).
# Then: python3 $S/visual_plan.py validate edit/<id> --card  → 0 errors (extend --dur / move --at until it passes).
source .claude/skills/webinar-shorts/scripts/env.sh
VP="python3 $S/visual_plan.py"
add(){ id=$1; shift; (cd "$REELS" && $VP add edit/$id --kind scene --mode overlay --box 60,240,900,340 --source speech "$@") || echo "!! add failed: $id $*"; }

# add w14-01 --type quote --at "word:definition#1" --dur 7.0 --source-ref "06:36-06:44" \
#   --lines "AI is in every stage of the cycle," "not just in the IDE" --accent "every stage" --label "SERHII IVANOV" \
#   --what "the definition as a quote" --why "the video's main thought"
# add w14-02 --type list --at "word:show#1" --dur 15.2 --source-ref "09:26-09:45" --lines "Not a buzzword if they show" \
#   --items-json '[{"text":"A written spec before code generation","at":"word:spec#1"},{"text":"Context files in the repo","at":"word:context#1"}]' \
#   --what "signs of a real AI SDLC" --why "readable without sound"
# add w14-04 --type stat --at "word:speed#1" --dur 5.0 --source-ref "26:24-26:28" \
#   --value-json '{"from":30,"to":40,"prefix":"+","suffix":"%"}' --lines "code writing speed" --what "+30-40%" --why "the key number"
