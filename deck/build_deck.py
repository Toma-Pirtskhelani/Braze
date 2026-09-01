import os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# -*- coding: utf-8 -*-
"""Assemble the presenting deck: visual slides + speaker-notes panel.

Slide modules are DISCOVERED, not listed: every deck/slides_*.py is imported in
filename order. Adding a chapter is one new file, with no edit here - which is what
stops the assembler drifting out of step with the content.
"""
import glob
import html
import json
import re
import sys

sys.path.insert(0, HERE)

import lib                                          # noqa: E402
from css import CSS                                 # noqa: E402

# The company is named in exactly one file. Fall back only if tools/ is absent.
sys.path.insert(0, os.path.join(REPO, "tools"))
try:
    import config                                   # noqa: E402
    TITLE, OUTPUT = config.DECK_TITLE, config.DECK_FILE
except Exception:                                   # noqa: BLE001
    TITLE, OUTPUT = "Analysis", "deck.html"

modules = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "slides_*.py")))
if not modules:
    raise SystemExit("no deck/slides_*.py found - there is nothing to build")
for m in modules:
    __import__(m)

S = lib.SLIDES
N = len(S)
if not N:
    raise SystemExit("slide modules imported but no slide called add() - nothing to build")

# guard: a dropped comma after a notes block silently swallows the grade and label
_bad = [(i + 1, sl["label"], sl["grade"]) for i, sl in enumerate(S)
        if not sl["label"] or sl["grade"] not in ("s", "m", "w")]
if _bad:
    raise SystemExit("slide with an empty label or invalid grade: %r" % (_bad,))


def notes_html(t):
    t = html.escape(t)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t, flags=re.S)


def ent(t):
    return t.replace("—", "&mdash;").replace("·", "&middot;").replace("’", "&rsquo;")


for _s in S:
    _s["label"] = ent(_s["label"])

sections = '\n'.join(s["html"] for s in S)

# guard: `.s` selects slides, so no other element may carry a bare `s` class
_bad = [m.group(0)[:70] for m in re.finditer(r'<(?!section)[a-z]+[^>]*class="([^"]*)"', sections)
        if 's' in m.group(1).split()]
if _bad:
    raise SystemExit("class collision with the slide selector: " + " | ".join(_bad))

ledger = ''.join(f'<div class="tk" data-g="{s["grade"]}" data-i="{i}"></div>' for i, s in enumerate(S))
gridit = ''.join(f'<div class="gi" data-i="{i}"><div class="gn">{i+1:02d}</div>'
                 f'<div class="gt">{s["label"]}</div></div>' for i, s in enumerate(S))
NOTES = json.dumps([notes_html(s["notes"]) for s in S])
LABELS = json.dumps([s["label"] for s in S])

DOC = f"""<title>{TITLE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Libre+Franklin:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
<div id="viewport"><div id="stage">
{sections}
<div id="ledger">{ledger}</div>
<div id="label"></div>
<div id="counter"></div>
</div></div>
<div id="notes"><h4>What to say</h4><div class="nb"></div></div>
<div id="grid"><h4>All {N} slides</h4><div class="gg">{gridit}</div></div>
<div id="help"><b>&larr; &rarr;</b> move &nbsp; <b>N</b> notes &nbsp; <b>G</b> overview &nbsp; <b>F</b> full screen</div>
<script>
const NOTES={NOTES}, LABELS={LABELS};
const slides=[...document.querySelectorAll('section.s')], n=slides.length;
const stage=document.getElementById('stage'), notes=document.getElementById('notes');
const grid=document.getElementById('grid'), nb=notes.querySelector('.nb');
const ticks=[...document.querySelectorAll('#ledger .tk')];
let i=0;
function fit(){{
  const pad = notes.classList.contains('on') ? 420 : 0;
  const w=(innerWidth-pad-64)/1280, h=(innerHeight-64)/720;
  const k=Math.min(w,h);
  stage.style.transform='scale('+k+')';
  document.getElementById('viewport').style.paddingRight=pad+'px';
}}
function show(k){{
  i=Math.max(0,Math.min(n-1,k));
  slides.forEach((s,j)=>s.classList.toggle('on',j===i));
  ticks.forEach((t,j)=>{{t.classList.toggle('cur',j===i);t.classList.toggle('seen',j<i);}});
  document.getElementById('counter').textContent=String(i+1).padStart(2,'0')+' / '+n;
  document.getElementById('label').innerHTML=LABELS[i]||'';
  nb.innerHTML=NOTES[i]||'<em style="color:#5D6675">No notes for this slide.</em>';
  location.hash=i+1;
}}
addEventListener('keydown',e=>{{
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){{e.preventDefault();show(i+1);}}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){{e.preventDefault();show(i-1);}}
  else if(e.key==='Home')show(0); else if(e.key==='End')show(n-1);
  else if(e.key==='n'||e.key==='N'){{notes.classList.toggle('on');fit();}}
  else if(e.key==='g'||e.key==='G')grid.classList.toggle('on');
  else if(e.key==='f'||e.key==='F'){{document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}}
  else if(e.key==='Escape')grid.classList.remove('on');
}});
ticks.forEach(t=>t.onclick=()=>show(+t.dataset.i));
document.querySelectorAll('#grid .gi').forEach(g=>g.onclick=()=>{{show(+g.dataset.i);grid.classList.remove('on');}});
addEventListener('resize',fit);
fit();
show(Math.max(0,(parseInt(location.hash.slice(1))||1)-1));
</script>"""

out = os.path.join(HERE, OUTPUT)
open(out, 'w', encoding='utf-8').write(DOC)
print("modules:", ", ".join(modules))
print("slides:", N)
print("bytes:", len(DOC))
missing = [k + 1 for k, s in enumerate(S) if not s["notes"]]
print("slides without notes:", missing or "none")
if lib.HELD:
    print("held back (hidden=True, still in source):", len(lib.HELD))
