# Industry Page Kit

The same service, retold in one vertical's language. A buyer from a narrow market checks one thing:
have you worked with people like me. A general service page cannot prove that. An industry page can —
if it is written with that industry's standards, cycles and units of measure.

Almost everyone falls into the same trap: the industry page is a copy of the service page with one
word swapped in the headline. The result is a duplicate that cannibalises its own parent, dilutes its
rankings and adds nothing for the buyer. That is why this Kit opens with a question about whether the
page should exist, not with a structure.

## G-I · Should this page exist at all

Run this **before** the questionnaire. Fail it and there is no page — there is a section on the parent
service page instead.

- [ ] **At least 2 cases from this vertical.** One case does not hold a page. Zero is fiction.
- [ ] **Demand exists** — queries carrying the industry name have volume, or the vertical drives ≥15%
      of pipeline.
- [ ] **Five facts that are not on the parent page** — a standard, a regulation, a unit of measure, a
      stakeholder, a procurement cycle, a typical timeline, a handover format. Fewer than five, write
      nothing.
- [ ] **The vertical's salesperson confirms** the objections here differ from the general ones.

> **The 60% rule.** At least 60% of an industry page must be unique against the parent service page.
> Only the process block and engagement models are shared. Below 60% it is a duplicate, and a
> duplicate is better unpublished.

**If it fails:** add a "We work with [industry]" section to the service page plus one case. Revisit
the standalone page when two cases exist.

## Structure — 15 slots

**1. Breadcrumbs** — `Home → Services → [Service] → [Industry]`. The hierarchy shows this is a branch
of the service, not a separate island.

**2. H1** — `[Service] for [industry] — [outcome in the industry's terms]`. Not "faster" but
"permit-ready set in three weeks".

**3. Hero with a vertical proof point** — one sentence on the service plus a number from *this*
industry: how many projects, in which regions, under which standards. The company-wide number does
not work here.

**4. Industry context — the main slot** — 3–5 specifics only someone who has worked in this market
knows: codes and regulations, who signs off and who blocks, the procurement cycle, units of measure,
file handover formats, seasonality. This slot is the entire reason the page exists separately.

**5. Pains of this vertical** — not the service's general pains, the ones that come up on calls in
this industry. Verbatim.

**6. What's included, in the industry's terms** — the same scope, named the way this buyer names it.
The same artifact is called different things in different markets; use theirs.

**7. Standards and compliance** — the codes, regulations, licences, insurance requirements you work
under. For technical services this is often the deciding block.

**8. Where the process differs** — do not restate the whole process. Show the 2–3 steps that run
differently here, and why.

**9. Cases from this vertical only** — minimum 2 cards with numbers and links. A case from an adjacent
industry breaks the page's entire promise.

**10. Client quote from the industry** — name, role, company from the same market.

**11. Tools, formats, integrations** — the software and formats this vertical uses. The signal is "we
are already inside your environment, no onboarding required".

**12. FAQ for the vertical** — regulatory, licensing, insurance, jurisdictional. The ones that are not
on the general service page.

**13. Action + form** — one primary action. The soft alternative is an industry checklist or a sample
work package.

**14. Other industries + parent service** — cards for sibling verticals and a link up to the service
page. Keeps the cluster connected.

**15. Hidden technical layer** — Service schema with `areaServed` and `audience`, FAQPage,
BreadcrumbList, canonical to self.

## Slots by category

| Category | Slots |
|---|---|
| **Proof of belonging** | industry context · standards · tools and formats · vertical cases · quote |
| **Offer clarity** | H1 formula · vertical pains · scope in their terms · where the process differs |
| **Conversion** | hero action · industry magnet · final form · sibling industries |
| **Search & AI visibility** | breadcrumbs · vertical FAQ · schema · canonical · link up to the service |

## Intake questionnaire — delivery lead + the vertical's salesperson

The point is to extract what is *not* on the parent page. Questions are deliberately narrow.

**A. Industry context** — Which codes, standards, regulations govern this market, and which come up on
calls? Who approves and who can block, and how does that differ from other industries? Typical cycle
from first contact to signature? What units do they measure results in? What seasonality or
regulatory deadlines drive timelines?

**B. Language** — What do they call what we deliver, verbatim? Which words from our service page are
meaningless to them? Three verbatim pain phrases from recent calls in this vertical.

**C. Differences in the work** — What runs differently in the process here, and why? What licences,
insurance, clearances are required of us? What software and handover formats does this vertical use?

**D. Proof** — How many projects in this industry, in which regions? Which 2–3 cases can be shown with
numbers? Which client from the vertical will give a quote with name and company?

**E. Objections** — Which questions get asked here and nowhere else? What killed deals specifically in
this vertical?

## Writer SOP

1. **Read the parent service page first.** Anything that could be copied from it must not be.
2. **Check the 60% rule before handover** — how many paragraphs have no equivalent on the parent page.
   Under 60%, go back for more material.
3. **Write in the industry's language.** Names of artifacts, roles and timelines come from the
   salesperson's answers, not from our internal glossary.
4. **Name standards precisely** — number, version, jurisdiction. A vague gesture at a standard is
   worse than omitting it.
5. **Only your own cases.** No two cases in the vertical means the page should not have passed G-I.
6. **Do not restate the whole process.** Differences only.
7. **FAQ stays narrow.** General questions belong on the service page.
8. **Links up are mandatory** — from the industry page to the parent service, and from the parent to
   every industry page.
9. **Mark visuals:** `[INDUSTRY HERO]`, `[CONTEXT]`, `[STANDARDS]`, `[PROCESS DIFFERENCES]`,
   `[CASE CARD]`, `[QUOTE]`.
10. **Run the humanisation pass** (`copy-humanisation.md`) as a separate step after the draft.
    Negative parallelism and punch triads are hard fails at the blind judge.
11. **Fact-check standards and figures** against the delivery lead. An invented standard costs the
    credibility of the whole page.

## Technical checklist

**URL and anti-cannibalisation** — `/services/service/industry/`, the industry page stays a branch of
the service · canonical to self, not to the parent · the parent service page links to all its
industry pages from an "Industries" block · run a cannibalisation check on the main queries after
indexing · search titles and descriptions differ between parent and child.

**Schema** — Service with `areaServed` and `audience` · FAQPage on the FAQ block · BreadcrumbList with
the full chain back to the service.

**Template** — "Other industries" block auto-selected by parent service · sticky CTA on mobile, short
form, analytics events · in sitemap, indexable, has inbound internal links.

## Designer brief

| Marker | What to produce |
|---|---|
| `[INDUSTRY HERO]` | First screen with imagery the vertical recognises plus that industry's number |
| `[CONTEXT]` | Industry realities block: icons or a stakeholder-and-cycle diagram |
| `[STANDARDS]` | Standards and clearances as chips, readable on mobile |
| `[PROCESS DIFFERENCES]` | Diagram with the diverging steps highlighted against the base process |
| `[CASE CARD]` | Vertical case card with number and link |
| `[QUOTE]` | Industry client pull quote with photo or logo |

Client's design system. The vertical's visual language comes through photography and diagrams, not
through changing the palette. Real artifacts from projects in this industry — stock imagery signals
you have not worked here. Alt text everywhere, mobile check.

## Pre-launch checklist

- [ ] G-I passed and the decision recorded
- [ ] 60% rule held
- [ ] Industry context carries ≥3 facts absent from the service page
- [ ] Standards named precisely (number, version, jurisdiction)
- [ ] 2+ cases from this vertical plus a quote
- [ ] FAQ is narrow, does not duplicate the service page
- [ ] Link up to the service and link down from the service to this page
- [ ] Canonical to self, schema validates
- [ ] Cannibalisation checked after indexing
- [ ] Mobile check
