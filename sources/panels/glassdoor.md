---
panel: Glassdoor
url: https://www.glassdoor.com/Overview/Working-at-Braze-EI_IE1024231.11,16.htm
status: EMPTY — awaiting capture
captured:
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
