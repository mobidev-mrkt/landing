#!/bin/bash
# Designed scenes for the w13b Shorts (Webinar 13, Ievgen and Helen). Run from reels/ with
# WEBINAR_SHORTS_ENV=../.claude/skills/webinar-shorts/scripts/env.sh
source "${WEBINAR_SHORTS_ENV:?set WEBINAR_SHORTS_ENV=<skill dir>/scripts/env.sh}"
VP="python3 $S/visual_plan.py"
add(){ id=$1; shift; (cd "$REELS" && $VP add edit/$id --kind scene --mode overlay --box 60,240,900,340 --source speech "$@") || echo "!! add failed: $id $*"; }
IEV="IEVGEN ZADOROZHNYI"; HEL="HELEN KHAILOVA-HORASH"

add w13b-01 --type quote --at "word:still#1" --offset -0.3 --dur 4.6 --source-ref "11:21-11:25" --lines "Your QA team can't handle" "all of that stuff" --accent "can't handle" --label "$IEV" \
  --what "the first bottleneck as a quote" --why "names the problem the hook asks about"
add w13b-01 --type stat --at "word:500#1" --dur 5.0 --source-ref "12:04-12:13" --value-json '{"from":100,"to":500}' --lines "lines of code from AI, instead of 100" \
  --what "500 vs 100 lines" --why "the number behind the code review bottleneck"

add w13b-02 --type list --at "word:reverse#1" --offset -0.3 --dur 23.0 --source-ref "32:58-33:27" --lines "Instead of a rewrite" \
  --items-json '[{"text":"Reverse engineering with AI","at":"word:reverse#1"},{"text":"Readable docs and business logic","at":"word:readable#1"},{"text":"Sequence and UML diagrams","at":"word:sequence#1"}]' \
  --what "what AI recovers from legacy code" --why "the practical answer to losing a vendor"

add w13b-03 --type quote --at "word:I#2" --offset -0.3 --dur 8.3 --source-ref "33:55-34:03" --lines "I would take a really skilled person" "who actually understands how to validate" "everything which AI gives me" --accent "validate" --label "$IEV" \
  --what "the main advice as a quote" --why "the line the video is about"
add w13b-03 --type list --at "word:relations#1" --offset -0.6 --dur 9.4 --source-ref "34:03-34:15" --lines "What to check" \
  --items-json '[{"text":"Relations","at":"word:relations#1"},{"text":"Diagrams","at":"word:diagrams#1"},{"text":"Documentation","at":"word:documentation#1"},{"text":"Hallucinations","at":"word:hallucinations#1"}]' \
  --what "what to validate" --why "turns the advice into a checklist"

add w13b-04 --type list --at "word:security#1" --offset -0.4 --dur 15.0 --source-ref "35:47-36:12" --lines "Ask your vendor" \
  --items-json '[{"text":"How they handle data security","at":"word:security#1"},{"text":"How they use AI","at":"word:using#1"},{"text":"Enterprise AI tools or cheap public models?","at":"word:enterprise#1"}]' \
  --what "three questions for the vendor" --why "the checklist a buyer can reuse"
add w13b-04 --type quote --at "word:cheap#2" --offset -1.0 --dur 4.4 --source-ref "36:20-36:25" --lines "They're cheap, free," "but your data will leak" --accent "data will leak" --label "$IEV" \
  --what "the risk as a quote" --why "the punchline of the clip"

add w13b-05 --type quote --at "word:exactly#1" --offset -0.6 --dur 4.8 --source-ref "37:12-37:16" --lines "AI will do exactly" "what you ask it to do" --accent "exactly" --label "$IEV" \
  --what "the core risk as a quote" --why "sets up the GitHub example"
add w13b-05 --type list --at "word:share#1" --offset -0.4 --dur 20.6 --source-ref "37:28-38:10" --lines "Rules your vendor should have" \
  --items-json '[{"text":"No company or client names in AI","at":"word:share#1"},{"text":"No budgets in AI","at":"word:budgets#1"},{"text":"All of it under NDA","at":"word:NDA#1"},{"text":"Human in the loop","at":"word:human#1"}]' \
  --what "the vendor rules" --why "an actionable checklist"

add w13b-06 --type list --at "word:changes#1" --offset -0.4 --dur 19.9 --source-ref "41:09-41:34" --lines "What AI speed really needs" \
  --items-json '[{"text":"Changes in your processes","at":"word:changes#1"},{"text":"Time and money","at":"word:time#1"},{"text":"Refactored legacy code","at":"word:refactored#1"},{"text":"AI on all SDLC stages","at":"word:Second#1"}]' \
  --what "the expectations list" --why "the four points of the answer"

add w13b-07 --type list --at "word:legacy#1" --offset -1.6 --dur 7.2 --source-ref "16:34-16:51" --lines "It's a completely different story" \
  --items-json '[{"text":"A legacy code base","at":"word:legacy#1"},{"text":"A massive undocumented system","at":"word:massive#1"}]' \
  --what "why legacy differs from a clean startup" --why "the contrast the clip makes"

add w13b-08 --type list --at "word:support#1" --offset -0.4 --dur 24.0 --source-ref "41:34-42:16" --lines "Budget for" \
  --items-json '[{"text":"Supporting the old system while you refactor","at":"word:support#1"},{"text":"Changes in your processes","at":"word:processes#1"},{"text":"Changes in team composition","at":"word:team#1"}]' \
  --what "the hidden costs" --why "readable without sound"
add w13b-08 --type quote --at "word:never#1" --offset -1.2 --dur 5.6 --source-ref "42:22-42:30" --lines "You never know how much AI" "will cost you in the future" --accent "cost you" --label "$IEV" \
  --what "the warning as a quote" --why "the line people remember"

add w13b-09 --type list --at "word:analyzing#1" --offset -0.4 --dur 11.8 --source-ref "07:05-07:19" --lines "AI in every SDLC stage" \
  --items-json '[{"text":"Business analysis and specs","at":"word:analyzing#1"},{"text":"Design","at":"word:designing#1"},{"text":"Architecture","at":"word:architect#1"},{"text":"Code and tests","at":"word:codes#1"},{"text":"Deploy and release","at":"word:deploys#1"}]' \
  --what "the five stages" --why "the definition as a checklist"

add w13b-10 --type list --at "word:preparation#1" --offset -0.3 --dur 6.5 --source-ref "42:52-43:00" --lines "To sum it up" \
  --items-json '[{"text":"Preparation","at":"word:preparation#1"},{"text":"Planning","at":"word:planning#1"},{"text":"Clean up","at":"word:clean#1"},{"text":"Correct implementation","at":"word:correct#1"},{"text":"Security","at":"word:security#1"}]' \
  --what "Helen's summary list" --why "the five points in one look"
add w13b-10 --type quote --at "word:AI#1" --offset -0.4 --dur 4.9 --source-ref "43:05-43:10" --lines "AI will bring you happiness." "Yeah, but at a cost." --accent "at a cost" --label "$HEL" \
  --what "the closing line as a quote" --why "the honest ending"
