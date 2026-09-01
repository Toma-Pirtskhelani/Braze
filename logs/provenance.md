# Provenance

What was captured, from where, on what date, and by what means. Every row in `data/` and
every file in `sources/` should be traceable to a line here.

**Append, never rewrite.** If a source is re-captured, add a new row rather than editing
the old one — the fact that a page changed between captures is itself evidence.

---

## Setup reconnaissance — 2026-09-01

Before any capture, each candidate source was probed to confirm it exists and to size
the job. **No content was extracted and nothing below is a finding about Braze** — these
describe the sources.

| Source | Address | Result |
|---|---|---|
| SEC company index | `sec.gov/files/company_tickers.json` | Braze, Inc. → CIK 1676238, ticker BRZE |
| SEC submissions | `data.sec.gov/submissions/CIK0001676238.json` | 737 filings, 2017-07-20 → 2026-08-28; FY ends 0131; SIC 7372 |
| SEC XBRL facts | `data.sec.gov/api/xbrl/companyfacts/CIK0001676238.json` | 1.3 MB, 357 us-gaap concepts; key series 2019-01-31 → 2026-04-30 |
| Docs sitemap | `braze.com/docs/sitemap.xml` | 200, 1,352 `<loc>` entries |
| Site sitemap index | `braze.com/sitemap.xml` | 200, index → 6 locale sitemaps → 6,366 distinct URLs |
| Docs page structure | `braze.com/docs/user_guide/...` | `<main>` container, single `<h1>`, meta description present |
| Status components | `braze.statuspage.io/api/v2/components.json` | 200, 132 components in 12 groups |
| Status incidents | `braze.statuspage.io/api/v2/incidents.json` + `/history.json` | 451 incidents, 2016-10-09 → 2026-08-05 |
| GitHub org | `api.github.com/orgs/braze-inc` | 137 public repos, org created 2017-10-16 |
| GitHub releases | `/repos/braze-inc/<sdk>/releases` | 494 releases across 9 SDK repos, 2016-12-13 → 2026-09-01 |
| Sub-processors | `braze.com/company/legal/subprocessors` | 200 |
| `security.txt` | `braze.com/.well-known/security.txt` | **200, 236 bytes — present** |
| Release notes | `braze.com/docs/help/release_notes/` | 200, redirects to `/docs/releases/home` |
| Release notes repo | `github.com/braze-inc/release-notes` | public, ~20 MB, pushed daily |
| Companies House | `find-and-update.company-information.service.gov.uk` | Two candidates: BRAZE LIMITED `09846844`, BRAZE MARKETING LTD `10711967`. **Neither confirmed as the vendor's** |
| crt.sh | `crt.sh/?q=%25.braze.com&output=json` | **HTTP 502 all afternoon** |
| Cert Spotter | `api.certspotter.com/v1/issuances` | 167 distinct DNS names on page 1, then HTTP 429 |
| G2 | `g2.com/products/braze/reviews` | **HTTP 403** to scripted access |
| Gartner Peer Insights | `gartner.com/reviews/...` | **HTTP 403** |
| Glassdoor | `glassdoor.com/Overview/Working-at-Braze-...` | **HTTP 403** |
| TrustRadius | `trustradius.com/products/braze/reviews` | **HTTP 403** |
| Investor relations | `investors.braze.com` | **HTTP 403**. Everything on it is in EDGAR; use EDGAR |

Tools were smoke-tested against these live endpoints; outputs were written to a scratch
directory and discarded, so `data/` and `sources/` ship empty.

---

## Capture log

_Append one section per capture run: date, tool, source, rows produced, failures._

<!--
## <date> — <tool>

| Source | Rows | Notes |
|---|---|---|
-->
