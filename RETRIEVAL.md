# Retrieval — how to search this corpus without loading it

The corpus will grow to tens of megabytes. **Never read a file end to end.** The habit
with the highest return in this whole method is one line:

```bash
rg -c -i 'PATTERN' sources/docs/ | sort -t: -k2 -rn | head
```

**Count first. Then read a bounded range.** Two files with forty hits is a different
finding from forty files with two hits, and that difference is often *the* finding.

---

## Looking for a number

Go to [`docs/FACTS.md`](docs/FACTS.md) and stop.

```bash
rg -i 'gross margin' docs/FACTS.md
```

If it is not there, find it, then **put it there** with a grade and a source path.

## Looking for a document

```bash
rg -i 'identity' data/docs_index.csv | cut -d, -f1,3        # find by title
rg -i 'segmentation' data/docs_index.csv | wc -l            # how many exist
awk -F, 'NR>1 {print $5}' data/docs_index.csv | sort | uniq -c | sort -rn | head -20   # sections
```

## Looking for where a topic lives, then reading it

```bash
rg -c -i 'rate limit' sources/docs/ | sort -t: -k2 -rn | head -10
rg -n -i 'rate limit' sources/docs/docs__api__basics.md | head          # get line numbers
sed -n '120,160p' sources/docs/docs__api__basics.md                     # read only that
```

The line numbers are your citation. `sources/docs/docs__api__basics.md:120-160`.

## Searching the derived tables

`data/` is CSV, so everything is one command.

```bash
head -1 data/financials_annual.csv | tr ',' '\n' | nl        # what columns exist
python3 -c "
import csv
for r in csv.DictReader(open('data/financials_annual.csv')):
    if r['period'].startswith('FY'):
        print(r['period'], r['GrossProfit'], r['ResearchAndDevelopmentExpense'])
"

rg -i '10-K' data/filings.csv | cut -d, -f1,2,8              # every annual report + URL
rg -i 'whatsapp' data/incidents.csv | wc -l                  # incidents naming a channel
sort -t, -k3 -rn data/capabilities.csv | head                # capabilities by focused pages
```

## Searching the panels

Review text is unstructured. Get context, not just the line.

```bash
rg -n -i -C2 'work.life' sources/panels/glassdoor.txt | head -40
rg -c -i 'segment' sources/panels/*.txt                      # which panel talks about what
```

**Do not hand-count themes.** Run `python3 tools/code_reviews.py` and cite the script.
The same corpus coded by hand three times produced three different answers on the
reference project.

## Searching the filings

The filing index is evidence before you open a document.

```bash
rg '^8-K' data/filings.csv | cut -d, -f2,6,8 | head -20      # material events, dated
rg 'DEF 14A' data/filings.csv | cut -d, -f2,8                # compensation and the board
```

To read a filing, take the `url` column and fetch it. 10-K risk factors are the honest
section: legally, they must disclose what could go wrong.

## Searching the timeline

```bash
rg '^2026-' data/timeline.csv | head -40                     # what happened this year
rg 'infrastructure' data/timeline.csv | tail -20             # newest hosts provisioned
```

**The newest CT entries are where unannounced things appear.** Read them first.

---

## Layout

```
sources/raw/         byte-exact original captures. Ugly names on purpose — renaming
                     them would break the byte-exact guarantee
sources/clean/       de-chromed captures under citable slugs
sources/docs/        the documentation corpus, YAML frontmatter + text
sources/panels/      G2 · Gartner · TrustRadius · Glassdoor · jobs. Capture date line 1
sources/external/    API spec, CT output, filings, probes
sources/ai-sessions/ other models' research, each with a fact-check header
sources/boilerplate.txt  the removed site chrome — kept once, because it contains
                         real claims and must be cited once rather than N times

data/                CSV only, all regenerable by tools/
docs/                written analysis and specifications
```

---

## The single most useful habit

Count before you read. It is the cheapest thing in this repository and it has produced
more findings than any amount of careful reading.

```bash
rg -c -i 'agentic' sources/docs/ | sort -t: -k2 -rn | head
```
