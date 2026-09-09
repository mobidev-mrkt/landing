# Handoff kit — shipping a page someone else will finish

A page that only runs on your laptop is not delivered. Most pages leave the production line
half-finished on purpose: proof is missing, payment links do not exist yet, the client's team will
move it into their CMS themselves. The handoff kit is what makes that state honest and workable
instead of a pile of files in a chat.

Use this whenever the page is being handed to another team — the client's marketer, an in-house
developer, an agency — rather than published by you.

---

## What ships

Five things. Nothing else is required, and a missing one is a real gap, not a formality.

| Artifact | Purpose |
|---|---|
| The page itself | Self-contained and openable with a double click. No build step, no package manager. |
| `README.md` | What is in the box, design tokens, page structure, how to move it into the target CMS. |
| `TODO.md` | Everything unfinished, ordered: blocking → placeholders → claims to verify → nice to have. |
| CMS split | The same page as separate markup / CSS / JS files, ready to paste into the target system. |
| Assets folder | Logos, icons, images actually referenced by the page, at the sizes used. |

---

## The placeholder registry

Every unfinished thing is visible **in the markup** and **in `TODO.md`**, using one pattern the
receiving team can search for. Square brackets work: `[PLACEHOLDER]`, `[Engineer name]`,
`[00 h]`, `[$0]`.

Rules that keep this honest:

- **A placeholder never looks finished.** An invented case study with plausible numbers is worse
  than an empty block, because nobody removes it.
- **Mocks are labelled on the artifact itself**, not only in the README. A sample report, dashboard
  or screenshot mock carries a visible line: "Illustrative example."
- **Each placeholder has an exit.** Either the real content, or "delete this section and its nav
  link". Never leave a block whose only future is being quietly published as is.
- **Named humans and quotes are never invented.** Roles and context are fine
  ("Solo founder · marketplace MVP · pre-launch"); invented names, faces and testimonials are
  fabricated proof and stay out even as filler.

---

## The blocker list

`TODO.md` opens with what blocks launch, and nothing else lives in that first section. Typical
blockers on a page that sells:

- Checkout or payment links not yet created → the page must **degrade gracefully**: an empty link
  falls back to the enquiry form, so the page is publishable before commerce is wired.
- Form destination: which plugin, endpoint or inbox actually receives it.
- Legal pages: the real permalinks, both in the footer and next to the order action.
- Any number that appears in two places in the source material with two different values. Do not
  silently pick one — put the conflict in the list.

Then, separately: claims that need the client's confirmation (years of experience, project counts,
delivery times, capacity limits). Those are theirs to stand behind, not yours to smooth over.

---

## The CMS split

Deliver the page twice: once as a working single file, once split for the target system.

```
page.html                  <- works standalone, this is what you demo
cms/
  page-content.html        <- body markup only, no <head>, no <style>, no <script>
  page.css
  page.js
  template.<ext>           <- optional native template that enqueues the two files
```

Non-obvious things that break this handoff, and belong in the README:

- **Asset paths.** The standalone page uses relative paths. The CMS will not. Say exactly which
  string to find-and-replace, and with what.
- **Class collisions.** Short names like `.btn`, `.wrap`, `.card` will collide with the theme.
  Offer the fix up front: wrap everything in one namespace class and prefix the selectors.
- **Duplicate chrome.** The page ships its own header and footer. Either it goes on a blank/canvas
  template, or those two blocks get deleted and the theme supplies them. Left unsaid, the client
  publishes a page with two headers and blames the page.
- **Cache busting.** Whatever the platform's version parameter is, name it and say to bump it.
- **Third-party embeds.** Any widget, review carousel or map that loads a remote script: name the
  network dependency, what the block looks like when it fails to load, and that consent tooling can
  block it. If the page has a cookie banner, that script is third-party by category.
- **Forms.** Static-host attributes (Netlify, Formspree and friends) mean nothing in a CMS. Say to
  replace the element with the platform's own form, and list the fields that must survive.

Verify the split before shipping: render the CMS version standalone and compare it to the original.
Same page height, same sections, no console errors. A split that was never rendered is a guess.

---

## README contents

Keep it to what a stranger needs on day one:

1. One paragraph: what this is, how to open it, that there is no build step.
2. File table.
3. **Before this goes live** — the blocking list, repeated from `TODO.md`. It is worth the
   duplication; nobody opens two files.
4. Design tokens: colours with hex, type scale, what the accent is allowed to do. The receiving
   team will add sections, and this is what keeps them on brand.
5. Page structure, section by section, in page order.
6. CMS instructions, per the split above.
7. Analytics, SEO and accessibility status: what is in place, what is deliberately absent, which
   viewports were tested.

Write it for the person who inherits this without you in the room. No "as discussed", no references
to conversations they never saw.

---

## Preflight before you send

- [ ] Page opens from the file system with no server and no errors in the console
- [ ] Every internal anchor resolves; no dead links
- [ ] No horizontal scroll at 375 / 768 / 1280 / 1440
- [ ] All images load, all have alt text, sizes are sane
- [ ] Every placeholder appears in `TODO.md`, and every `TODO.md` entry exists in the markup
- [ ] Nothing confidential in the package: other clients' names, internal notes, keys, staging URLs
- [ ] CMS split rendered and compared against the original
- [ ] Archive is one folder, named for the project, without dev-only helper scripts
