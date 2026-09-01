# dist — published deliverables

Empty until the research runs. Cut a release with:

```bash
bash tools/make_release.sh            # dates it today
bash tools/make_release.sh 2026-10-01 # or name the date
```

That produces four files plus a zip, all dated:

| File | What it is |
|---|---|
| `Braze-Competitor-Analysis-Deck-<date>.html` | The deck, self-contained. `N` notes · `G` grid · `←→` move |
| `Braze-Competitor-Analysis-Deck-<date>.pdf` | One page per slide, 1280×720, text layer intact |
| `Braze-Evidence-Record-<date>.html` | The record, self-contained |
| `Braze-Evidence-Record-<date>.pdf` | A4 portrait, printable |
| `Braze-Analysis-<date>.zip` | All four, for sending |

**Nothing in a release differs from the source documents** except the print stylesheet
and the embedded fonts. The release script rebuilds the deck from `deck/slides_*.py`
first, so a release cannot be stale.

## What the script verifies, and why

- **No fallback fonts.** Chrome's `--print-to-pdf` silently drops variable fonts and
  falls back to Georgia and Menlo. The script fetches static faces using an old
  user-agent string and inlines them as data URIs, then reads the font list back out of
  the PDF bytes. Georgia or Menlo in that list means the step failed — and it is easy to
  miss by eye.
- **Page count matches the slide count**, read from the built deck rather than hardcoded.
  A hardcoded count goes stale the first time a slide is added, and then verifies nothing.
- **A text layer exists** (`/ToUnicode`), so the PDF is searchable rather than an image.

Requires Google Chrome at the standard macOS path.
