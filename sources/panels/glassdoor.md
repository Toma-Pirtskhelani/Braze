---
panel: Glassdoor
url: https://www.glassdoor.com/Reviews/Braze-Reviews-E1879400.htm
status: captured (Tier 2, signed-in browser — full aggregate stats, a 5-review sample;
  not all 524)
captured: 2026-09-02
---

# Glassdoor — paste target

This file is a **pre-created target**. `tools/code_reviews.py` skips it while `status`
says EMPTY, so an unfilled panel never silently becomes a zero in a count.

## What to capture

1. Overall rating, % recommend, CEO approval
2. The sub-ratings, especially **work/life balance** — and its trend over time
3. Recent review bodies: pros, cons, advice to management

## How to fill it

1. Open the URL above in a browser you are already signed in to.
2. Select the review text and paste it below the line.
3. Change `status:` above to `captured` and put today's date in `captured:`.

Separate individual reviews with a blank line — `code_reviews.py` splits on
blank-line groups, and one record per review is what makes the percentages mean
anything.

**Do not summarise. Paste the raw text.** A summary is already an analysis, and the
whole point of coding a corpus with a script is that nobody's judgement gets in
between the reviews and the count.

────────────────────────── PASTE BELOW THIS LINE ──────────────────────────

Attempted via claude-in-chrome (Tier 2, operator's signed-in Chrome) on 2026-09-02.
IMPORTANT: the URL pre-set at the top of this file (EI_IE1024231) now resolves to an
unrelated company ("Hokulia Shave Ice") — Glassdoor's numeric employer ID appears to
have been reassigned or was wrong at file creation. The correct, current company page,
found via Glassdoor's own search, is:

    https://www.glassdoor.com/Overview/Working-at-Braze-EI_IE1879400.11,16.htm
    https://www.glassdoor.com/Reviews/Braze-Reviews-E1879400.htm

Both the Overview and Reviews pages for the correct company immediately show a
non-dismissible "Learn more about Braze with a free account" / "Keep browsing Braze
reviews with a free account" modal that blocks all page content (confirmed via
get_page_text: the extracted text is only the modal's own copy, nothing from the page
behind it). Per AGENTS.md, Tier 2 does not log in, accept terms, or solve a CAPTCHA — so
this correctly escalates to TIER 3. No review bodies, rating breakdown, or work-life
sub-ratings were captured.

## What is available without logging in (from Glassdoor's own search results page,
## https://www.glassdoor.com/Search/results.htm?keyword=Braze — not walled)

- Braze: 4.1 out of 5 stars, 563 reviews, 284 jobs listed, 1.3K salaries reported
- (Distinct company entries also matched "Brazen Technologies" 4.0★/37 reviews and
  "Brazen Animation" 3.5★ — neither is Braze, listed here only so a future capture
  does not confuse them)

## TIER 3 — RESOLVED 2026-09-02

The operator created a Glassdoor account and signed in to the browser claude-in-chrome
drives. Re-attempted Tier 2 on both URLs above: the sign-in wall is gone, both pages
render fully. Everything below was captured signed-in, no data was entered by the agent
(the account's own login state was already present in the browser), and nothing was
paywalled beyond a "load more"-style cutoff after 5 reviews on the default view.

## Aggregate stats (Overview + Reviews pages, signed in)

- 4.1 out of 5 stars, based on 524 ratings
- 82% would recommend to a friend
- 90% approve of CEO (Bill Magnuson)
- 71% positive business outlook

### Glassdoor AI-summarized culture themes (from the Reviews page, "What employees say
### about culture at Braze", sourced from 4+ reviews per Glassdoor's own citation)

- **Work environment & culture** — "Braze is celebrated for its exceptional culture,
  emphasizing collaboration, kindness, and a sense of purpose. Employees appreciate the
  supportive atmosphere and the genuine care shown by colleagues, which fosters
  community and engagement."
- **Management & leadership** — "While many praise approachable leadership, some
  reviews highlight challenges with management effectiveness, particularly regarding
  decision-making and clarity in direction. There's a desire for more strategic
  communication to align teams and enhance focus."
- **Career & growth** — "Employees recognize opportunities for professional development
  and advancement, but some express concerns over limited upward mobility and
  discrepancies in compensation relative to market rates."
- **Work-life balance** — "The company offers a strong work-life balance with flexible
  policies, though experiences can vary by team. Many appreciate the emphasis on
  employee well-being, despite some reports of heavy workloads during busy periods."

### Ratings trend, last 6 months (Apr–Sep 2026), read off the site's own chart

- Overall: ~4.2 (Apr) → ~4.1 (May) → ~4.05 (Jun) → ~4.05 (Jul) → ~4.1 (Aug) → ~4.1 (Sep) —
  essentially flat, a slight dip and recovery, not a decline
- Work/Life balance: tracks almost identically to Overall over the same window — ~4.1
  (Apr) dipping to ~4.0 (Jun) and recovering to ~4.1 by Sep. No divergence between the
  two lines worth calling a trend on its own.

### Ratings by demographic group — Race/Ethnicity (as shown; other tabs — Gender, Sexual
### orientation, Disability, Parental status — exist but were not opened)

- Asian: 4.3★ (16 ratings)
- Hispanic or Latinx: 4.2★ (7 ratings)
- White: 3.7★ (57 ratings)
- Black or African American: no ratings shown

## Individual reviews (raw text, "most recent" sort, the 5 shown before the feed cuts
## off into other page modules — not all 524)


Title: "Solid culture and work-life balance, but pay issues"
Reviewer: Senior business systems analyst — Current employee, more than 3 years — New
York, NY — Aug 17, 2026
Rating: 4.0/5 — Recommend: yes — CEO approval: yes — Business outlook: positive

Pros: Good work life balance, good sales team and culture
Cons: Pay, too much red tape, and trying to hire too many salesforce people


Title: "Good pay and work-life balance, but slow bureaucracy"
Reviewer: Anonymous employee — Current employee — Aug 10, 2026
Rating: 5.0/5 — Recommend/CEO approval/Business outlook: not marked by this reviewer

Pros: Good / Good pay / Work life balance
Cons: Lost leadership / Beauracracy [sic] / Slow, red tape


Title: "This is the review headline"
Reviewer: Director growth — Former employee — New York, NY — Aug 5, 2026
Rating: 5.0/5 — Recommend/CEO approval/Business outlook: not marked

Pros: Good feedback when it comes to pros
Cons: Bad feedback when it comes to cons

Note: this review's title and body both read as unfilled placeholder text ("This is the
review headline" / "Good feedback when it comes to pros" / "Bad feedback when it comes
to cons") — it carries no substantive content. Recorded verbatim rather than dropped,
since the instruction is to paste raw text and let the coding script decide, but anyone
reading review_coding.csv should know this record contributes a rating with no real
signal behind it.


Title: "Good (for now)"
Reviewer: Anonymous employee — Current employee, more than 3 years — Aug 2, 2026
Rating: 4.0/5 — Recommend: yes — CEO approval: yes — Business outlook: positive
Sub-ratings: Work/Life balance 4.0, Culture & values 4.0, Diversity & inclusion 3.0,
Career opportunities 3.0, Compensation and benefits 4.0

Pros: The Braze culture is unbeatable, this is the best company I've worked for.
Cofounders are awesome, tech is ahead of the martech game, colleagues are mostly
intelligent and want to make a difference.

Cons: New leadership team (CPO CIO CRO CMO CFO), so expect changes. There seems to be a
power struggle internally. Only time will tell. If you joined post IPO, your salary is
probably below average. (Folks who joined pre-ipo had a great run, but they're also
mostly gone). Career options limited, and there's a limit to number of folks who can
score a 4/5 and above. Largely dependent on your manager to fight for your appraisal.
Also, only 1 promotional cycle per year and majority of the bonus is given end of FY.


Title: "Good team collaboration, but onboarding needs improvement"
Reviewer: Technical support — Former employee, more than 3 years — Las Vegas, NV — Jul
29, 2026
Rating: 4.0/5 — Recommend: yes — CEO approval: neutral/not held — Business outlook: not
marked

Pros: Benefits, team and collaboration are good
Cons: Training/ onboarding, communication, and processes could've been better
