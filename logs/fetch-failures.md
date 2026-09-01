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
| `g2.com/products/braze/reviews` | HTTP 403 | **Needs a human or a browser session** |
| `gartner.com/reviews/.../braze` | HTTP 403 | Same. Capture the **shortlists** — highest-value field on the page |
| `trustradius.com/products/braze/reviews` | HTTP 403 | Same |
| `glassdoor.com/Overview/Working-at-Braze-...` | HTTP 403 | Same |
| `investors.braze.com` | HTTP 403 | **Not needed.** Everything on it is in EDGAR |

---

## Run log

_Appended by the tools._
