# Fetch failures

**A gap you have written down is evidence. A gap you have not is a mistake.**

Every source that failed, with the URL, the error, the date, and whether it was retried.
`tools/fetch_docs.py` and `tools/ct_probe.py` append here automatically; add manual
failures yourself.

Before the deliverable ships, every row here needs one of three outcomes:

- **retried and succeeded** — note the date and move on
- **permanently unavailable** — state it in the deck as an absence, with what it would
  have told you
- **needs a human** — a browser session or a paste, listed in `TODO.md`

---

## Known at setup — 2026-09-01

| Source | Error | Status |
|---|---|---|
| `crt.sh/?q=%25.braze.com&output=json` | HTTP 502 Bad Gateway, sustained | **Outstanding.** crt.sh is frequently down; retry. Cert Spotter is the fallback |
| `api.certspotter.com/v1/issuances` | HTTP 429 after ~1 page | **Partial.** Anonymous callers are rate-limited; a free `CERTSPOTTER_TOKEN` lifts it |
| `g2.com/products/braze/reviews` | HTTP 403 | Resolved via Tier 2 browser, 2026-09-02 — see Run log below |
| `gartner.com/reviews/.../braze` | HTTP 403 | Resolved via Tier 2 browser, 2026-09-02 — shortlist captured — see Run log below |
| `trustradius.com/products/braze/reviews` | HTTP 403 | Resolved via Tier 2 browser, 2026-09-02 — see Run log below |
| `glassdoor.com/Overview/Working-at-Braze-...` | HTTP 403 | Resolved via Tier 2 browser after the operator signed in, 2026-09-02 — see Run log below |
| `investors.braze.com` | HTTP 403 | **Not needed.** Everything on it is in EDGAR |

---

## Run log

_Appended by the tools._

### 2026-09-02 — full pipeline run, escalation ladder worked for the four review panels

`SEC_CONTACT` was set for this run (`Toma Pirtskhelani toma.pirts@gmail.com`);
`GITHUB_TOKEN` and `CERTSPOTTER_TOKEN` were not, so `github_org.py`/`fetch_issues.py` ran
at the unauthenticated 60 req/hr limit and `ct_probe.py`'s Cert Spotter fallback ran at
the anonymous rate limit — both still completed (`data/repos.csv`, `data/issues.csv`,
833 hosts in `data/subdomains.csv`, all via the `certspotter` fallback since crt.sh
itself returned its usual 502). Setting those two tokens would very likely widen the
GitHub and CT coverage on a rerun; this is a substitution, not a loss — see
`AGENTS.md` §Substitutions.

- **G2, Gartner Peer Insights, TrustRadius** — Tier 1 (script) still 403s, as recorded
  above. **Tier 2 (operator's browser, claude-in-chrome) succeeded without logging in**
  and captured a partial sample into `sources/panels/{g2,gartner,trustradius}.md`:
  overall rating and full star distribution for all three; G2's coded pros/cons tags;
  TrustRadius's synthesized pros/cons and a coded 36%-cite-weak-reporting stat; Gartner's
  full "customers also considered" shortlist (Salesforce, Adobe, Iterable, Oracle,
  Optimove, Blueshift, MoEngage, CleverTap) — the field AGENTS.md flags as highest-value
  because no vendor-controlled source has it. Full review bodies beyond the first one or
  two per site are paywalled behind each site's own sign-in wall; per the ladder, Tier 2
  does not cross that. **Outcome: retried and succeeded (partial).**
- **Glassdoor** — Tier 1 still 403s. **Tier 2 escalated correctly to Tier 3**: both the
  Overview and Reviews pages for the correct company
  (`glassdoor.com/.../Braze-...-E1879400...`) show a non-dismissible sign-in wall — the
  page serves *only* the modal's own text, confirmed via `get_page_text`. No login,
  terms-acceptance, or CAPTCHA was attempted, per AGENTS.md. Recorded in
  `sources/panels/glassdoor.md`: the public search-result snapshot only (4.1★, 563
  reviews, 284 jobs, 1.3K salaries, from `glassdoor.com/Search/results.htm`). **Outcome:
  needs a human** — the operator can sign in and paste below the line in that file;
  everything else in the pipeline proceeds without it.
- **Also found and fixed while on Glassdoor**: the pre-set URL in
  `sources/panels/glassdoor.md` (`EI_IE1024231`) had drifted to an unrelated company
  ("Hokulia Shave Ice"). Corrected to `EI_IE1879400`, found via Glassdoor's own company
  search. Anyone revisiting a pre-set panel URL should re-verify the company name on the
  landing page before trusting the ID.
- **2026-09-02, later the same day** — the operator created a Glassdoor account and
  signed in to the browser claude-in-chrome drives, then asked for a retry. The wall was
  gone on both the Overview and Reviews pages. Captured into
  `sources/panels/glassdoor.md`: 4.1★/524 ratings, 82% recommend, 90% CEO approval, 71%
  positive outlook, the full 4-theme AI-summarized culture breakdown (including
  work-life balance and its 6-month trend, which tracks flat alongside the overall
  rating — no divergence worth calling a trend), a demographic-group rating breakdown,
  and 5 full review bodies (the page's default view before it hands off to other
  modules — not all 524). `code_reviews.py` rerun afterward: 860 total records coded
  (up from 855), Glassdoor contributing 6 (5 reviews + the aggregate summary block,
  since it's long enough to pass the 60-character/record-length floor). **Outcome:
  retried and succeeded**, no longer needs a human.
- **Careers board** (`braze.com/company/careers`, not blocked, not in the table above) —
  captured via Tier 2: the full department taxonomy (15 functions) and location
  taxonomy (26 sites) from the board's own filter widgets, plus a 2-page/24-role sample
  of the ~284-300 total open roles. The department-filter checkboxes did not reliably
  narrow results when driven by click automation in this session, so no exact
  per-department headcount split was captured — only the taxonomy and an unrepresentative
  (front-of-list) role sample. **Outcome: partial — an exact department histogram would
  need either a retry of the filter UI or a direct read of the Greenhouse board API.**
