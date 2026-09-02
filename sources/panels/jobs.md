---
panel: Careers board
url: https://www.braze.com/company/careers
status: EMPTY — awaiting capture
captured:
---

# Careers board — paste target

This file is a **pre-created target**. `tools/code_reviews.py` skips it while `status`
says EMPTY, so an unfilled panel never silently becomes a zero in a count.

## What to capture

1. Every open role, with its function and location
2. The **split by function** is the finding: where headcount goes is the strategy, stated in hiring
3. Any role naming a technology, a region, or a product not yet announced

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
