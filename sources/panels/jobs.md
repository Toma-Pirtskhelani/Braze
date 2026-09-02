---
panel: Careers board
url: https://www.braze.com/company/careers
status: captured (partial — full department/location taxonomy, a 2-page sample of roles;
  not all ~25 pages)
captured: 2026-09-02
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

Captured via claude-in-chrome (Tier 2, operator's signed-in Chrome, no login required)
from https://www.braze.com/company/careers on 2026-09-02, via the embedded Greenhouse
job board (job-boards.greenhouse.io/braze). The board paginates at 12 roles/page across
25 pages — full department- and location-filter taxonomies were read from the page's
own filter widgets (exhaustive), but individual role listings below are a 2-page sample
(pages 1-2 of 25), not all ~284-300 roles. The filter checkboxes could not be reliably
driven by click automation in this session (selections did not visibly narrow the
results), so an exact per-department count is not included here — anyone wanting the
precise histogram should apply the Department filter directly at the URL above.

## Scale

- ~25 result pages at 12 roles/page ≈ 284-300 open roles, consistent with the "284 jobs"
  figure Glassdoor's own company-search listing showed for Braze on the same date.

## Department taxonomy (exhaustive — all filter options on the board)

Business Development, Customer Experience, Engineering, Finance, Growth, GTM Operations,
GTM Strategy, Information Technology, Legal, Marketing, Partnerships, People, Product,
Sales, Solutions Consulting.

## Location taxonomy (exhaustive — all filter options on the board)

Atlanta, Austin, Australia, Berlin, Boston, Bucharest, Chicago, Denver, Dubai, Jakarta,
London, Madrid, Mexico, Munich, New York City, Paris, Remote - Spain, Remote - USA, San
Francisco, São Paulo, Seoul, Singapore, Sydney, Tokyo, Toronto, Vancouver.

## Sample roles (page 1 of 25, default/unfiltered sort — appears grouped by department)

1. Senior Business Development Representative — Business Development — Berlin
2. Senior Business Development Representative — Business Development — Berlin
3. Business Development Representative — Business Development — London
4. Director, Business Development JAPAC — Business Development — Singapore
5. Business Development Representative — Business Development — São Paulo
6. Data Scientist II (AI Deployment) — Customer Experience — São Paulo
7. Technical Account Manager — Customer Experience — New York City
8. Technical Account Manager — Customer Experience — Austin
9. Technical Account Manager — Customer Experience — Chicago
10. Technical Account Manager — Customer Experience — San Francisco
11. AI Decisioning Technical Lead — Customer Experience — Tokyo
12. Team Lead, Email Deliverability — Customer Experience — Chicago

## Sample roles (page 2 of 25)

13. Data Scientist, AI Ongoing Delivery — Customer Experience — London
14. Team Lead, Email Deliverability — Customer Experience — Austin
15. Team Lead, Email Deliverability — Customer Experience — New York City
16. Team Lead, Email Deliverability — Customer Experience — San Francisco
17. Forward-Deployed Data Scientist — Customer Experience — Tokyo
18. Support Engagement Lead — Customer Experience — Austin
19. Support Engagement Lead — Customer Experience — Chicago
20. Support Engagement Lead — Customer Experience — San Francisco
21. Support Engagement Lead — Customer Experience — New York City
22. Support Engagement Lead — Customer Experience — Denver
23. Customer Success Manager, Global SMB — Customer Experience — Jakarta
24. Senior Technical Support Specialist — Customer Experience — Tokyo

Note: because the board appears sorted with Business Development first and Customer
Experience next, this consecutive 2-page sample is NOT a representative cross-section of
the 15 departments — it is heavily weighted toward Business Development and Customer
Experience roles, many of them AI-adjacent (Data Scientist, AI Decisioning, Forward-
Deployed Data Scientist), several duplicated across US cities (a hiring pattern, not 5
distinct roles). Do not extrapolate department-share percentages from this sample; use
only the exhaustive department taxonomy above for "which functions Braze hires for," and
say the per-department count is not captured rather than estimate it.
