# sources/media — where each image came from

Captured 2026-09-02. Like everything else in `sources/`, these files are **immutable**:
`tools/build_assets.py` reads them and writes `deck/assets.py`, and nothing edits them
in place. Re-fetching is how you update one.

Every image here is used **nominatively** — to identify the company or person being
discussed, at the point they are discussed. None is presented as this project's own
brand, none is altered beyond trimming transparent margins and resizing, and the deck
states on its title slide that it is a competitor analysis built from public sources.

| File | Source | Grade | Used on |
|---|---|---|---|
| `braze-logo.png` | `https://www.braze.com/_next/static/media/logo.15~1jid2_k4jj.png` — the wordmark in braze.com's own site header | claimed (company-own marketing asset) | slides 1, 6 |
| `offerfit-logo.png` | `https://web.archive.org/web/20241231032519/https://www.offerfit.ai/` → `images.ctfassets.net/.../OfferFit_logo_og.png` | claimed (company-own, via Internet Archive) | slide 9 |
| `ceo-magnuson.png` | `https://s25.q4cdn.com/307167611/files/images/management/new/Bill-Magnuson.png`, from `investors.braze.com/governance/leadership` | claimed (company-own investor-relations page) | slide 7 |
| `founders-2011-techcrunch-disrupt.png` | `https://cdn.sanity.io/images/b7pblshe/marketing-prod/b2d779ffa73781d5915d2435f5f245ccac50f162-1102x828.png`, from `braze.com/company` under "How it started" | claimed (company-own marketing page) | **captured, not used** — see below |

## Two notes that matter

**The OfferFit logo is not on the live web.** `offerfit.ai` resolves, but it now serves a
Braze page titled *"1:1 Personalization at Scale | BrazeAI Decisioning Studio™"* with
Braze's own wordmark in the header. The logo had to come from an Internet Archive capture
dated 2024-12-31. That is itself corroboration for the reading in `deck/record/03-acquisitions.md`
§3.1: the $0.9m the purchase-price allocation assigned to trademarks said nobody expected
the OfferFit name to survive, and it has not.

**No North Star Y logo could be sourced, and none is used.** `northstary.com`,
`northstary.com.au` and `north-star-y.com` do not resolve and have no Internet Archive
captures; a web search returns only Braze's own 2023 press releases. The brand appears to
have been retired completely on acquisition, as OfferFit's was. Rather than attach a logo
belonging to some other company called "North Star" — of which there are several, none
verifiably Braze's ANZ reseller — slide 10 carries no logo, and the absence is stated in
the record. **Attaching an unverified mark to a named company would be a fabricated
identification, which is precisely the error this project exists to avoid.**

## The photograph that was captured and is not in the deck

`founders-2011-techcrunch-disrupt.png` was sourced, encoded and placed on slide 7, then
removed. The reason is design rather than evidence: it put a **second photographic
treatment** on a slide that already carried a circular portrait, at a different width, and
the original is a low-resolution capture with cropped lettering along its top edge. One
photographic treatment per slide — the rule is in `deck/COMPONENTS.md`.

The file stays here because it *is* evidence: it is the image Braze publishes under "How
it started", and it is the only photograph of the founding pair on any Braze property.
`tools/build_assets.py` names it in a comment with what it would take to restore it.

## Why it was never captioned by name

`founders-2011-techcrunch-disrupt.png` shows two people. Braze's own alt text is
`"CEO and CTO"` and the page copy reads *"Braze CEO Bill Magnuson and CTO Jon Hyman
participated in a 2011 hackathon…"* — but the source does **not** say which figure is
which. While it was in the deck it was captioned as a pair, never left-to-right. The
portrait that remains on slide 7 is the one Braze publishes with a name attached to it.
