# Measuring what a vendor actually ships

The central measurement of the method, and the one that produces the headline finding
more often than anything else.

## The problem

Every vendor claims every capability. Marketing pages are free to write, so a feature
that shipped last month and a feature with a decade of engineering behind it get the
same page, the same confidence, and often the same logo treatment.

## The insight

**Documentation volume is a proxy for what a vendor has to support.**

Nobody writes five hundred pages for a feature that does not exist. And nobody writes
fifteen pages for the thing they renamed the company around unless it is newer and
thinner than the renaming implies. Documentation is written for people who will hit the
limits; it has to describe the product that is really there.

## The focused-page test

A page counts for a capability only if the capability's vocabulary appears **at least
five times in its body**.

That threshold is deliberately strict, and it is what makes the number defensible.
Without it, every page carrying a nav menu counts for everything. With it, "mentions
email" and "is about email" become different measurements — and the ratio between two
capabilities becomes something anyone can re-run and get.

```bash
python3 tools/capability_count.py            # or --min N to move the threshold
```

The pattern set lives in a visible taxonomy file, and the regex that produced each row
is written into the output CSV, **precisely so a reader can disagree with it**. A
measurement whose method is hidden is an assertion.

## What it does not measure

Say these out loud when you present the number. They are what stop it being challenged.

- **It measures documentation, not capability.** A thin section can mean an immature
  feature or a genuinely simple one. Say which you think it is, and why.
- **A new feature is under-documented by construction.** Date the corpus and check the
  release notes before reading thinness as weakness.
- **The pattern set is a judgement.** It is visible for exactly that reason.
- **Vendors document differently.** Cross-vendor comparison of raw page counts is
  meaningless. Compare *within* one vendor, between capabilities.

## The second lens: published API surface

Count endpoints per capability from the API reference. A capability with substantial
documentation and **zero dedicated endpoints** is a capability you cannot build on — and
that gap, when it exists, is usually the sharpest single line in the analysis.

This lens is independent of the first: documentation is written by technical writers,
the API surface by engineers, and neither is derived from the other.

## The third lens: the words customers use

Code the review corpus for capability vocabulary and compare the distribution against
the documentation distribution. If a vendor's positioning is 40% about one capability
and 10% of customer language mentions it, that is a finding — and it comes from people
with no stake in the vendor's narrative.

Lock the coding in a script. The same reviews coded three times by hand produce three
different answers; that happened, and reconciling them cost more than the counting did.

## The fourth lens: analyst coverage counts

Review panels record how many reviewers rated each capability. Those counts measure
**what customers actually deployed enough to have an opinion about**. A capability rated
by 56 reviewers against one rated by 236 is a deployment-share signal from a source the
vendor did not write.

## Presenting it

**Only present a capability finding when at least two lenses agree, and say which.**
Four independent lenses agreeing is close to unfalsifiable. One lens alone is a
measurement in search of a conclusion.

And bound the claim. Never *"their AI is thin"* — it is wrong, it credits nothing, and a
competent counterpart will rebut it in one sentence. Instead:

> A decade of real shipped machine learning — 231 focused pages on recommendations, 19
> documented algorithms, a training system running 2,500 models a week — **and** an
> agentic layer they renamed the entire company around with 15 focused pages and zero
> dedicated API endpoints, against 517 pages for email.

Every number in that sentence is re-derivable, it credits what deserves credit, and
there is nothing in it to argue with.
