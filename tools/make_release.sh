#!/usr/bin/env bash
# Cut a dated release of the deck and the evidence record: HTML + PDF + zip.
#
# Usage:  bash tools/make_release.sh [YYYY-MM-DD]
#
# Why this script exists: rendering these two documents to PDF took several failed attempts to
# get right, and the reasons are not obvious. They are recorded inline below so nobody has to
# rediscover them.

set -euo pipefail
cd "$(dirname "$0")/.."
REPO="$PWD"
DATE="${1:-$(date +%F)}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "Google Chrome not found at $CHROME"; exit 1; }

echo "── rebuilding both documents from source"
python3 deck/build_deck.py
python3 deck/make_script.py
python3 deck/build_record.py

DECK="$REPO/deck/braze-deck.html"
REC="$REPO/deck/evidence-record.html"
OUT="$REPO/dist"
mkdir -p "$OUT"

cp "$DECK" "$OUT/Braze-Competitor-Analysis-Deck-$DATE.html"
cp "$REC"  "$OUT/Braze-Evidence-Record-$DATE.html"

# ── The three things that make the PDF render correctly ──────────────────────
#
# 1. STATIC FONTS, NOT VARIABLE ONES.  Chrome's --print-to-pdf silently drops variable fonts and
#    falls back to Georgia/Menlo, which looks wrong and is easy to miss. Google Fonts serves
#    static WOFF only to an older user agent, so fetch the CSS as Firefox 27 and inline every
#    face as a data: URI. This is the single non-obvious step.
#
# 2. PRINT CSS THAT UNSTACKS THE DECK.  On screen one slide is visible at a time (opacity/
#    visibility, absolutely positioned inside a scaled #stage). For print each section has to
#    become its own 1280x720 page with the transform removed.
#
# 3. print-color-adjust: exact.  Without it the dark deck prints white.
#
echo "── fetching static font faces"
python3 - "$WORK" <<'PY'
import re, sys, urllib.request, base64, os
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:27.0) Gecko/20100101 Firefox/27.0'}
get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
work = sys.argv[1]
SETS = {
  'deck':  'Instrument+Serif:400,400italic|Libre+Franklin:400,500,600,700|JetBrains+Mono:400,500',
  'record':'JetBrains+Mono:400,500,600|Newsreader:400,500,600,700|Public+Sans:400,500,600,700',
}
for name, fam in SETS.items():
    css = get('https://fonts.googleapis.com/css?family=' + fam).decode()
    cache = {}
    def repl(m):
        u = m.group(1)
        if u not in cache:
            cache[u] = "url(data:font/woff;base64,%s) format('woff')" % base64.b64encode(get(u)).decode()
        return cache[u]
    css = re.sub(r"url\((https://fonts\.gstatic\.com/[^)]+)\)\s*format\('woff'\)", repl, css)
    assert 'gstatic' not in css, 'a font url was not inlined'
    open(os.path.join(work, name + '.css'), 'w').write(css)
    print('   %s: %d faces' % (name, css.count('@font-face')))
PY

echo "── building print copies"
python3 - "$WORK" "$REPO" <<'PY'
import re, sys, os
work, repo = sys.argv[1], sys.argv[2]

DECK_PRINT = '''<style id="printcss">@media print{
  @page{size:1280px 720px;margin:0}
  *{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;transition:none!important;animation:none!important}
  html,body{height:auto!important;overflow:visible!important;background:var(--ink)!important}
  #viewport{position:static!important;display:block!important;background:none!important;place-items:initial!important;inset:auto!important}
  #stage{position:static!important;width:auto!important;height:auto!important;transform:none!important;box-shadow:none!important;background:none!important}
  section.s{position:relative!important;inset:auto!important;opacity:1!important;visibility:visible!important;transform:none!important;
    width:1280px!important;height:720px!important;display:flex!important;background:var(--ink)!important;overflow:hidden!important;
    break-after:page;page-break-after:always}
  section.s:last-of-type{break-after:auto;page-break-after:auto}
  #help,#notes,#grid,#label,#counter,#ledger{display:none!important}
  .pfoot{display:flex!important;position:absolute;left:74px;right:74px;bottom:32px;align-items:center;justify-content:space-between;
    font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.1em}
  .pfoot .pf-rule{flex:1;height:2px;margin:0 16px;background:var(--line);border-radius:1px}
  .pfoot .pf-rule i{display:block;height:2px;background:var(--line2);border-radius:1px}
}
@media screen{.pfoot{display:none}}</style>
<script>(function(){function b(){var s=document.querySelectorAll('#stage section.s'),n=s.length;
for(var i=0;i<n;i++){if(s[i].querySelector('.pfoot'))continue;var f=document.createElement('div');f.className='pfoot';
f.innerHTML='<span>'+(s[i].getAttribute('data-t')||'')+'</span><span class="pf-rule"><i style="width:'+(((i+1)/n)*100).toFixed(2)+'%"></i></span><span>'+String(i+1).padStart(2,'0')+' / '+n+'</span>';
s[i].appendChild(f);}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',b);else b();
window.addEventListener('beforeprint',b);})();</script>'''

REC_PRINT = '''<style id="printcss">@media print{
  @page{size:A4 portrait;margin:15mm 14mm 16mm}
  *{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  html{scroll-behavior:auto}
  body{font-size:9.6pt;line-height:1.5;background:var(--paper)!important}
  nav.parts{display:none!important}
  .w{max-width:none!important;padding:0!important}
  body > .w > header{break-after:page;page-break-after:always}
  section.part{break-before:page;page-break-before:always;break-inside:avoid}
  .box,.tw,table,pre,.thesis{break-inside:avoid;page-break-inside:avoid}
  tr,li{break-inside:avoid;page-break-inside:avoid}
  thead{display:table-header-group}
  h1,h2,h3,h4,.thesis{break-after:avoid;page-break-after:avoid}
  h1{font-size:26pt}h2{font-size:17pt}h3{font-size:13pt}h4{font-size:8.4pt}
  .thesis{font-size:10.4pt}table{font-size:8.6pt}.tw table td,.tw table th{padding:4px 6px}
  code,.mono{font-size:8.2pt}a{text-decoration:none}
  a[href^="http"]::after{content:" (" attr(href) ")";font-size:7pt;color:var(--muted);word-break:break-all}
  a[href^="#"]::after{content:""}
}</style>
<script>document.documentElement.setAttribute('data-theme','light');</script>'''

def prep(src, out, fonts_css, print_css, anchor, extra_attr=''):
    s = open(src, encoding='utf-8').read()
    i = s.index(anchor)
    head, body = s[:i], s[i:].replace('</body></html>', '')
    head = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', head)
    head = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>',
                  '<style id="inlinefonts">' + fonts_css + '</style>', head, count=1)
    assert 'fonts.googleapis' not in head, 'font link not replaced'
    open(out, 'w', encoding='utf-8').write(
        '<!doctype html><html lang="en"%s><head><meta charset="utf-8">\n' % extra_attr
        + head + print_css + '\n</head><body>\n' + body + '\n</body></html>')

fd = open(os.path.join(work, 'deck.css')).read()
fr = open(os.path.join(work, 'record.css')).read()
prep(os.path.join(repo, 'deck/braze-deck.html'),  os.path.join(work, 'print-deck.html'),
     fd, DECK_PRINT, '<div id="viewport">')
prep(os.path.join(repo, 'deck/evidence-record.html'),   os.path.join(work, 'print-record.html'),
     fr, REC_PRINT, '<nav class="parts">', ' data-theme="light"')
print('   print copies written')
PY

echo "── rendering PDFs"
"$CHROME" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf="$OUT/Braze-Competitor-Analysis-Deck-$DATE.pdf" \
  "file://$WORK/print-deck.html" >/dev/null 2>&1
"$CHROME" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf="$OUT/Braze-Evidence-Record-$DATE.pdf" \
  "file://$WORK/print-record.html" >/dev/null 2>&1

echo "── verifying"
# the expected page count is READ FROM THE BUILT DECK, never hardcoded: a hardcoded
# count silently goes stale the first time a slide is added, and then verifies nothing.
SLIDES=$(grep -o '<section class="s' "$DECK" | wc -l | tr -d ' ')
echo "   deck declares $SLIDES slides"
python3 - "$OUT" "$DATE" "$SLIDES" <<'PY'
import re, sys, os
out, date, slides = sys.argv[1], sys.argv[2], int(sys.argv[3])
for f, want_pages in [('Braze-Competitor-Analysis-Deck', slides), ('Braze-Evidence-Record', None)]:
    p = os.path.join(out, '%s-%s.pdf' % (f, date))
    d = open(p, 'rb').read()
    pages = len(re.findall(rb'/Type\s*/Page[^s]', d))
    fonts = sorted({m.group(1).decode().split('+')[-1] for m in re.finditer(rb'/BaseFont\s*/([A-Za-z0-9+,\-]+)', d)})
    bad = [x for x in fonts if x.startswith(('Georgia', 'Menlo', 'Times', 'Helvetica'))]
    print('   %-42s %3d pages  %d fonts%s' % (os.path.basename(p), pages, len(fonts),
          '  ** FALLBACK FONTS: %s **' % bad if bad else ''))
    assert b'/ToUnicode' in d, 'no text layer in ' + p
    if want_pages: assert pages == want_pages, 'expected %d pages, got %d' % (want_pages, pages)
PY

cd "$OUT"
rm -f "Braze-Analysis-$DATE.zip"
zip -q -X "Braze-Analysis-$DATE.zip" \
  "Braze-Competitor-Analysis-Deck-$DATE.pdf" "Braze-Evidence-Record-$DATE.pdf" \
  "Braze-Competitor-Analysis-Deck-$DATE.html" "Braze-Evidence-Record-$DATE.html"

echo
echo "release $DATE:"
ls -la | grep "$DATE" | awk '{printf "   %-52s %7.0f KB\n", $9, $5/1024}'
