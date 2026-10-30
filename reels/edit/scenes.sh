#!/bin/bash
# Designed scenes for the 10 Shorts (visual_plan.py add); texts from the speech, see edit/cut-plan.md
S=/root/.claude/plugins/synced/c347354c-4cb9-45b3-b39b-0ac1576e85d9_7e769f59-ffb2-4b04-a2ff-96c3350fa29f/c1ae3d1a-cbd2-4ee3-be95-a87be163ba1f/skills/it-reelsmaker/scripts
VP="python3 $S/visual_plan.py"
SER="SERHII IVANOV"
IEV="IEVGEN ZADOROZHNYI"
add(){ id=$1; shift; $VP add edit/short$id --kind scene --mode overlay --box 60,240,900,340 --source speech "$@" || echo "!! add failed: $id $*"; }

add 01 --type list --at "word:redoing#1" --dur 8.6 --source-ref "06:15-06:28" --lines "What slowed delivery" \
  --items-json '[{"text":"Redoing work over and over","at":"word:redoing#1"},{"text":"Waiting for a spec","at":"word:waiting#1"},{"text":"Waiting for QA","at":"word:QA#1"}]' \
  --what "list of what blocked delivery" --why "turns the problem into three readable items"
add 01 --type quote --at "word:definition#1" --dur 7.05 --source-ref "06:36-06:44" --lines "AI is in every stage of the cycle," "not just in the IDE" --accent "every stage" --label "$SER" \
  --what "the definition as a quote" --why "the video's main thought, named speaker"

add 02 --type list --at "word:show#1" --dur 15.2 --source-ref "09:26-09:45" --lines "Not a buzzword if they show" \
  --items-json '[{"text":"A written spec before code generation","at":"word:spec#1"},{"text":"Context files in the repo","at":"word:context#1"},{"text":"Reviewers responsible for the files","at":"word:reviewers#1"}]' \
  --what "three signs of a real AI SDLC" --why "the practical test, readable without sound"

add 03 --type quote --at "word:back#1" --dur 5.4 --source-ref "24:33-24:39" --lines "The generation literally got slower" "but the quality was much better" --accent "much better" --label "$SER" \
  --what "the key observation as a quote" --why "the paradox the video is about"
add 03 --type list --at "word:speed#1" --dur 7.0 --source-ref "24:47-24:54" --lines "The adoption curve" \
  --items-json '[{"text":"Speed goes up","at":"word:speed#1"},{"text":"Then slows down","at":"word:slow#1"},{"text":"Then grows again","at":"word:grows#1"}]' \
  --what "three stages of the curve" --why "the curve is easier to see than to hear"

add 04 --type stat --at "word:speed#1" --dur 5.0 --source-ref "26:24-26:28" --value-json '{"from":30,"to":40,"prefix":"+","suffix":"%"}' --lines "code writing speed" \
  --what "+30-40% code writing speed" --why "the number the argument starts from"
add 04 --type stat --at "word:degrades#1" --dur 5.5 --source-ref "26:31-26:36" --value-json '{"from":0,"to":50,"prefix":"−","suffix":"%"}' --lines "code review and QA verification" \
  --what "-50% review and QA throughput" --why "the bottleneck number"

add 05 --type list --at "word:cleans#2" --dur 16.4 --source-ref "40:06-40:20" --lines "The window robot" \
  --items-json '[{"text":"Cleans one window","at":"word:cleans#2"},{"text":"Stops","at":"word:stops#1"},{"text":"Asks you to turn it off","at":"word:crying#1"},{"text":"You carry it to the next window","at":"word:next#2"}]' \
  --what "the robot story step by step" --why "makes the analogy concrete"
add 05 --type quote --at "word:robot#1" --dur 6.2 --source-ref "40:40-40:45" --lines "It requires a lot of manual work" "which can be automated" --accent "manual work" --label "$SER" \
  --what "the takeaway as a quote" --why "links the analogy to AI SDLC"

add 06 --type quote --at "word:this#1" --dur 5.2 --source-ref "14:42-14:48" --lines "The initial project is not ready" "for AI integration" --accent "not ready" --label "$IEV" \
  --what "the diagnosis as a quote" --why "the main claim, named speaker"
add 06 --type list --at "word:bugs#1" --dur 13.3 --source-ref "14:50-15:10" --lines "New features on old code" \
  --items-json '[{"text":"More bugs","at":"word:bugs#1"},{"text":"More bottlenecks","at":"word:bottlenecks#1"},{"text":"The old code base cannot support it","at":"word:support#1"}]' \
  --what "consequences of building on unrefactored legacy" --why "three effects, readable without sound"

add 07 --type quote --at "word:guesses#1" --dur 3.6 --source-ref "17:40-17:44" --lines "It guesses" "and guesses very convincingly" --accent "convincingly" --label "$SER" \
  --what "the core problem as a quote" --why "the line people will remember"
add 07 --type list --at "word:fix#1" --dur 7.9 --source-ref "18:23-18:31" --lines "The fix: four steps" \
  --items-json '[{"text":"Give it context","at":"word:give#1"},{"text":"Set the rules","at":"word:set#1"},{"text":"Lock the current behavior","at":"word:lock#1"},{"text":"Define a pattern","at":"word:then#1"}]' \
  --what "the four steps" --why "an actionable checklist"

add 08 --type quote --at "word:back#1" --dur 3.4 --source-ref "20:15-20:19" --lines "Zero value," "a lot of effort" --accent "Zero value" --label "$SER" \
  --what "the result of the big-bang migration" --why "the punchline of the story"
add 08 --type list --at "word:migrated#1" --dur 10.5 --source-ref "20:28-20:41" --lines "What worked" \
  --items-json '[{"text":"Migrate one part","at":"word:migrated#1"},{"text":"Review it with the team","at":"word:reviewed#1"},{"text":"Agree on a pattern","at":"word:agreed#1"},{"text":"Repeat in small batches","at":"word:repeat#1"}]' \
  --what "the safe migration, step by step" --why "the lesson as a checklist"

add 09 --type list --at "word:first#1" --dur 14.0 --source-ref "20:55-21:13" --lines "3 questions" \
  --items-json '[{"text":"Can AI see the whole system?","at":"word:see#1"},{"text":"Does it know your rules?","at":"word:know#1"},{"text":"Will you notice if it breaks something?","at":"word:notice#1"}]' \
  --what "the three questions" --why "the checklist the video promises"

add 10 --type stat --at "word:half#1" --dur 5.6 --source-ref "29:40-29:44" --value-json '{"from":0,"to":50,"prefix":"~","suffix":"%"}' --lines "of the code was dead" \
  --what "roughly half of the code was dead" --why "the surprise number"
add 10 --type stat --at "word:15#1" --dur 3.6 --source-ref "29:54-30:00" --value-json '{"from":1,"to":15}' --lines "user roles in a simple service" \
  --what "15 roles" --why "the second surprise"
