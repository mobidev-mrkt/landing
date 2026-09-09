# Open items before launch

Ordered by what blocks the test.

## Blocking

- [ ] **Stripe Payment Links** for the three tiers → paste into `CHECKOUT_LINKS` in `index.html` (and `wordpress/vibecode-audit.js`).
- [ ] **Form destination**: WP form plugin shortcode, or a real endpoint. Right now the form submits nowhere.
- [ ] **Legal links**: point footer + form consent line at the real WordPress permalinks.
- [ ] **Confirm prices**: page uses $399 / $899 / $1,099. The pain-point table in the source doc says $499 / $999 / $1,199.

## Placeholders in the markup (search for `[`)

- [ ] Success story: `[PLACEHOLDER] Payments broke on launch day…` + four empty metrics `[00]`, `[00 h]`, `[0%]`, `[$0]`. Real case, or delete the section and its nav link.
- [ ] Who reads your code: `[Engineer name]`, `[Role, e.g. …]`, `[Years in production software…]` ×3, plus real photos in place of the silhouette avatars.
- [ ] Sample report mock: labelled "Illustrative example". Replace with a real anonymised report page if one can be shared.

## Claims to verify with the client

- [ ] "10+ years in software development" and "30+ code-rescue projects" (hero trust row).
- [ ] "Up to 50,000 lines of code" as the tier-1 boundary.
- [ ] Delivery times: 1 / 2 / 3 business days.
- [ ] The three quotes in "The problem" are paraphrased inbound messages, attributed by role only. If they are not real inbound, reword the section subhead.

## Nice to have

- [ ] Open Graph / Twitter card image once the final URL exists.
- [ ] GA4 or GTM, wired to the client's consent setup.
- [ ] Thank-you page or inline success state after the form submits.
- [ ] A short case or logo note explaining that the marquee logos are MobiDev clients, not buyers of this audit.

---

# webinar-ai-native-speed.html — "AI-Native Speed on a Legacy Codebase" (Sep 30)

## Blocking

- [ ] **Speaker photos.** ~~Three `[ph]` avatar placeholders~~ real photos added for Serhii Ivanov, Ievgen Zadorozhnyi, Helen Khailova-Horash — confirm the client is OK with the AI-cutout + unified-background treatment before launch.
- [x] ~~Form destination~~ — embeds the real HubSpot form (portal 47062060, form 171392a6-a943-4b51-80a7-548dac1f8200); confirmed live on the actual HubSpot landing page (contentId 221489397169), fields and button render styled correctly.
- [x] ~~HubSpot consent text~~ — already says "Privacy Policy and Cookie Policy" in the live form, no Terms of Service mentioned. Nothing to change.
- [ ] **Form's rich-text intro is unedited placeholder copy.** The live form shows the literal HubSpot default text "This is a rich text area, you can add whatever copy you like" above the name fields. This lives inside the FORM itself (Marketing > Forms > this form in the HubSpot portal), not in the page — there's no API/MCP tool available here to edit form field content, so **edit or delete that rich-text block directly in the HubSpot form editor** before launch.

## Claims to verify

- [ ] Confirm final speaker titles (Head of Resource Management / Delivery Manager at MobiDev / Senior Solutions Manager) match what goes on the internal brief doc.
