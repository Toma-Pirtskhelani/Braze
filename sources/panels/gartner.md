---
panel: Gartner Peer Insights
url: https://www.gartner.com/reviews/market/multichannel-marketing-hubs/vendor/braze
status: EMPTY — awaiting capture
captured:
---

# Gartner Peer Insights — paste target

This file is a **pre-created target**. `tools/code_reviews.py` skips it while `status`
says EMPTY, so an unfilled panel never silently becomes a zero in a count.

## What to capture

1. Overall rating and number of ratings
2. **The shortlists — 'customers also considered'. This is the single highest-value field on any review site**, because the vendor did not choose it
3. Deployment region / country per reviewer, where given
4. Coverage counts per capability (how many reviewers rated each one)
5. Reasons for purchase, if the panel reports them

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
