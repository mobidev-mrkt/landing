# Gates and scorecards

Four gates and one scorecard. They exist because the expensive failures on a website are decided
before the writing starts and after it finishes, not during.

| Gate | When | Blocks |
|---|---|---|
| **G-I** | first, industry pages only | the page existing at all |
| **G-A** | before the first word | writing |
| **G-T** | before publish | publishing, on technical grounds |
| **G-J** | after G-T | publishing, on quality — scored by a model that did not build the page |

---

## G-I · Should this page exist (industry pages only)

Runs first, before anything else, and only for industry/vertical pages. Full detail in
`kit-industry-page.md`.

- [ ] 2+ cases from this vertical
- [ ] Demand: queries with the industry name, or ≥15% of pipeline
- [ ] 5 facts absent from the parent service page
- [ ] The vertical's salesperson confirms different objections
- [ ] The 60% uniqueness rule can realistically be met

**Fail →** a section on the parent service page instead. Revisit when two cases exist.

---

## G-A · Architecture gate — before the first word

Runs for every page type.

- [ ] **Placed in the blueprint.** The page has a parent, a cluster and a final URL. If the blueprint
      does not exist, stop: build it first.
- [ ] **Cannibalisation checked.** No existing page already targets these queries. If one does, the
      decision is rewrite-and-merge, not publish-alongside.
- [ ] **Inbound internal links identified.** Name the specific existing pages that will link here. A
      page with no inbound link is invisible.
- [ ] **Baseline captured** in Search Console if the URL already existed — impressions, position,
      clicks. Without a baseline the 90-day review cannot say whether the rewrite helped.

**Why this gate is first:** a page that duplicates an existing one costs the entire writing cycle and
also drags down the page it duplicates. Rewriting after publication is more expensive than deciding
before.

---

## G-T · Technical gate — before publish

- [ ] Indexable, present in sitemap, canonical points where intended
- [ ] Schema validates for every type used on the page
- [ ] Performance and accessibility within threshold; mobile checked on a real viewport
- [ ] One primary conversion action; analytics events verified firing by hand, not assumed
- [ ] All `[markers]` replaced with final visuals; alt text everywhere

---

## G-J · Blind judge — after G-T, before publish

The page is scored by a **fresh model that did not build it**. The builder never marks its own work
up: after two hours inside a page, every compromise has a reason attached to it, and reasons are
exactly what a scorecard is supposed to ignore.

### What the judge receives

- The page draft in full
- The page type and the Kit's slot list
- The scorecard below, whichever applies
- A fact sheet for what it cannot see from the copy: final URL, canonical target, schema types
  present, measured performance numbers, viewport widths checked, contrast results, and whether
  analytics events were verified by hand. Anything unverified is labelled unverified.

### What the judge must NOT receive

- The intake answers and the reasoning behind them
- The gate justifications
- Which Kit slots were dropped and why — the dropped-slot excuse is the main way a self-scorer
  launders a gap into a decision
- Any opinion from the builder about how the page turned out

### What the judge returns

JSON only, no prose:

```json
{
  "scores": {"<axis>": 0},
  "total": 0,
  "hard_fails": [],
  "lowest": "<axis>",
  "one_fix": "<one concrete edit>"
}
```

Axes and weights come from the scorecard. Grade harshly: partial credit per axis, with the lost
points attributable.

### Hard fails — any one of these fails the gate regardless of total

- [ ] A figure, client name, certification or standard that cannot be traced to a source
- [ ] Negative parallelism ("not X, but Y") or a rule-of-three punch triad anywhere in the copy
- [ ] No price and no range on a service or landing page
- [ ] More than one primary conversion action
- [ ] Zero or more than one `<h1>`
- [ ] A `[placeholder]` marker left in the page
- [ ] Contrast or keyboard operation failing

### The loop

**Gate = `total ≥ 85` AND `hard_fails` empty.**

Not taken → fix every hard fail first, then apply `one_fix` to the `lowest` axis, then rescore with a
**new** subagent. Never re-ask the same judge: a judge shown its own suggestion applied grades the
suggestion, not the page.

Stop after three rounds. Still short → hand over flagged "gate not taken — X/85, weakest axis =
&lt;axis&gt;" and let the author decide. Publishing below 85 without saying so is forbidden.

---

## Scorecard — service page and most types

Threshold **85 / 100**. Below it, return to the axis that lost points. Do not average a failure away.

| Axis | Weight | What is checked |
|---|---|---|
| Conversion | 20 | one action, soft alternative, short form, events working |
| Offer clarity | 15 | what's included, the boundary, process, price, buyer's language |
| Structure | 15 | every Kit slot present or deliberately dropped |
| Search and AI visibility | 15 | queries, FAQ, schema, quotable blocks |
| Human copy | 10 | no AI tells, varied rhythm, an opinion and a boundary present |
| Proof | 10 | cases from this service, figures, quote, team |
| Design and UX | 10 | client design system, mobile, hierarchy, accessibility |
| Technical layer | 5 | URL, canonical, performance, indexation |

Technical carries only 5 because G-T already blocks publication on it. Scoring it heavily here would
count the same check twice and let a page buy its way to 85 on plumbing.

## Scorecard — industry page

Different weights: the risks here are duplication and unproven belonging, not offer clarity.

| Axis | Weight | What is checked |
|---|---|---|
| Uniqueness against the parent page | 20 | 60% rule, different search titles, no cannibalisation |
| Proof of belonging to the industry | 20 | context, standards, 2+ vertical cases, quote, tools |
| Conversion | 15 | one action, industry magnet, form, events |
| Copy in the industry's language | 10 | buyer's terms, verbatim pains |
| Human copy | 10 | no AI tells, varied rhythm, an opinion and a boundary present |
| Search and AI visibility | 10 | industry-name queries, FAQ, schema |
| Place in the cluster | 10 | link up and down, sibling block, breadcrumbs |
| Design and technical layer | 5 | design system, mobile, performance, indexation |

## Scoring the Human copy axis

Full rubric and the tell list are in `copy-humanisation.md`.

| Points | State |
|---|---|
| 9–10 | No banned tells. Rhythm varies. Specifics, an opinion and a stated boundary all present. |
| 6–8 | One or two isolated tells, or clean but flat — no opinion, uniform rhythm. |
| 3–5 | Tells recur across sections, or the page reads as a filled template. |
| 0–2 | Negative parallelism or punch triads present, brochure adjectives throughout. Hard fail. |

## How to score honestly

Award partial credit per axis and write down what was lost and why. A scorecard that always returns
95 measures nothing.

Three habits that keep it useful:

- **Blind, always.** A score produced by the builder is not a measurement.
- **Score before the fixes, not after.** The first number is the one that tells you where the process
  is weak across many pages.
- **Track the losing axis across pages.** If "proof" keeps losing points, the problem is not the
  writer — it is that nobody is collecting case studies. If "human copy" keeps losing them, the
  drafting prompt is doing the damage upstream.

---

## Post-launch review — 30 and 90 days

Against the baseline captured at G-A.

| Signal | What it means | Action |
|---|---|---|
| Impressions growing, position flat | The page is found but not chosen | Title and description rewrite |
| Position growing, no enquiries | Traffic arrives, the offer does not land | Conversion and copy pass |
| Nothing at 90 days | Wrong place in the cluster, or no demand | Review the blueprint, consider merging |
| Parent page dropped after a child launched | The child is a duplicate | Fold it back into a section |

The last row matters most for industry pages and is the reason the uniqueness axis carries the
heaviest weight there.
