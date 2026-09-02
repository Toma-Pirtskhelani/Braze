# -*- coding: utf-8 -*-
"""Presenting-deck builder: visual slides + speaker notes."""
import html as _h
from icons import icon as _icon

SLIDES=[]

def esc(t): return t

HELD = []   # written, verified, and deliberately kept out of the running deck

def add(html, notes="", grade="s", label="", hidden=False):
    """hidden=True keeps the slide in the source and out of the deck.
    Nothing is deleted, so restoring it is a one-word change."""
    rec = {"html":html,"notes":notes.strip(),"grade":grade,"label":label}
    (HELD if hidden else SLIDES).append(rec)

# ---------- components ----------
def head(eyebrow, headline, sub=None):
    o=f'<div class="head"><div class="eyebrow">{eyebrow}</div><h2>{headline}</h2>'
    if sub: o+=f'<p class="kick">{sub}</p>'
    return o+'</div>'

def figs(items, size="", cols=None, focus=None):
    """items: (value, label) or (value, label, kind), kind in '', 'neg', 'boxed'.

    focus=i marks item i (0-based) as the one being pointed at. Emphasis is carried by
    VALUE, not hue: the focused figure stays bright and its siblings dim. Grade colours
    (green/amber/red) are reserved for the evidence system, so a big number is never
    tinted amber and mistaken for a source grade. 'neg' stays red, which reads as a
    warning rather than as a grade.
    """
    out=''
    for i,it in enumerate(items):
        v,l = it[0],it[1]; k = it[2] if len(it)>2 else ''
        if focus is not None and i!=focus and k!='neg': k += ' dim'
        out+=f'<div class="fig {size} {k}"><div class="fv">{v}</div><div class="fl">{l}</div></div>'
    n = cols or len(items)
    return f'<div class="figrow" style="grid-template-columns:repeat({n},1fr)">{out}</div>'

def divider(pn, title, questions, foot=None, extra=""):
    li=''.join(f'<li><span class="qn">{i:02d}</span>{q}</li>' for i,q in enumerate(questions,1))
    f=f'<div class="foot">{foot}</div>' if foot else ''
    return (f'<div class="pn">{pn}</div><h2>{title}</h2><ul>{li}</ul>{f}{extra}')

def stats(items, big=False):
    sz="huge" if big else ""
    c=''.join(f'<div class="stat {sz}"><div class="n">{n}</div><div class="l">{l}</div></div>' for n,l in items)
    return f'<div class="statrow" style="grid-template-columns:repeat({len(items)},1fr)">{c}</div>'

def tiles(items, cols=3, size=24):
    """items: (icon-name, title, description). The icon is an SVG key from icons."""
    c=''
    for i,t,d in items:
        glyph = _icon(i, size=size) if i else ''
        c+=(f'<div class="tile"><div class="ti">{glyph}</div><div class="tt">{t}</div>'
            + (f'<div class="td">{d}</div>' if d else '') + '</div>')
    return f'<div class="tiles" style="grid-template-columns:repeat({cols},1fr)">{c}</div>'

def bars(items, unit=""):
    """items: (label, value) neutral, or (label, value, colour-token) to emphasise."""
    items=[(i[0], i[1], (i[2] if len(i)>2 else 'bar')) for i in items]
    mx=max(v for _,v,_ in items) or 1
    rows=''
    for lab,val,col in items:
        w=max(1.2, val/mx*100)
        vs='' if col=='bar' else ' style="color:var(--%s)"' % col
        rows+=('<div class="barrow"><div class="bl">%s</div>'
               '<div class="bt"><div class="bf" style="width:%.1f%%;background:var(--%s)"></div></div>'
               '<div class="bv"%s>%s%s</div></div>' % (lab, w, col, vs, val, unit))
    return '<div class="bars">%s</div>' % rows

def flow(steps, key=(), mark=None):
    """steps: (n, title, detail). key={i,...} gives a neutral accent.
    mark={i:'s'|'m'|'w'} colours a step to match the card that discusses it, so the
    flow and the commentary below it are read as one thing."""
    mark = mark or {}
    c=''
    for i,(n,t,d) in enumerate(steps,1):
        cls=''
        if i in mark: cls=' mk-'+mark[i]
        elif i in key: cls=' key'
        c+=(f'<div class="step{cls}"><div class="si">{n}</div><div class="st">{t}</div>'
            + (f'<div class="sd">{d}</div>' if d else '') + '</div>')
    return f'<div class="flow" style="grid-template-columns:repeat({len(steps)},1fr)">{c}</div>'

def timeline(items, total=False):
    """items: (date, value, caption). total=True marks the LAST item as an
    accumulation of the others rather than another event on the line."""
    c=''
    for i,(d,v,cap) in enumerate(items):
        last = total and i==len(items)-1
        cap_html = f'<div class="tlc">{cap}</div>' if cap else ''
        c+=(f'<div class="tlitem{" tot" if last else ""}"><div class="tld">{d}</div>'
            f'<div class="tlv">{v}</div>{cap_html}</div>')
    cls='timeline'+(' has-total' if total else '')
    cut=f';--tlcut:{100.0/len(items):.4f}%' if total else ''
    return f'<div class="{cls}" style="grid-template-columns:repeat({len(items)},1fr){cut}">{c}</div>'

def logos(names, cols=6, accent=()):
    c=''.join(f'<div class="logo{" acc" if n in accent else ""}">{n}</div>' for n in names)
    return f'<div class="logos" style="grid-template-columns:repeat({cols},1fr)">{c}</div>'

def cards(items, cols=3):
    c=''.join(f'<div class="card {k}"><h3>{t}</h3><p>{b}</p></div>' for t,b,k in items)
    return f'<div class="cards" style="grid-template-columns:repeat({cols},1fr)">{c}</div>'

def big(text, sub=None):
    o=f'<div class="bigline">{text}</div>'
    if sub: o+=f'<div class="bigsub">{sub}</div>'
    return o

def split(left,right,ratio="1fr 1fr"):
    return f'<div class="split" style="grid-template-columns:{ratio}">{left}{right}</div>'

def figurehead(src, name, role, note, foot=None, alt=None):
    """A named person: circular portrait, name, role, a line of substance, a footnote.

    css.py has styled .figurehead and .portrait since the scaffold was ported; nothing
    used them, because nothing in this analysis named a human being until the proxy was
    read properly. Only use this where the SOURCE names the person in the image. A face
    with a caption is an assertion about identity, and it takes a grade like any other.
    """
    o = (f'<div class="figurehead"><img class="portrait" src="{src}" '
         f'alt="{alt or name}"><div><div class="fname">{name}</div>'
         f'<div class="frole">{role}</div><div class="fnote">{note}</div>')
    if foot: o += f'<div class="fedu">{foot}</div>'
    return o + '</div></div>'

# ---------- world map (equirectangular dot grid) ----------
_BOX=[
 # North America
 (-168,-141, 55, 71),(-141,-125, 52, 70),(-125,-102, 49, 70),(-102,-60, 47, 68),
 (-125,-95, 32, 49),(-95,-75, 30, 47),(-84,-77, 25, 32),(-118,-93, 23, 33),
 (-105,-83, 14, 23),(-92,-77,  7, 18),(-120,-70, 68, 79),
 # Greenland and the Arctic islands
 (-52,-22, 60, 82),(-45,-25, 76, 84),(-100,-62, 70, 80),
 # South America
 (-81,-50,  0, 12),(-79,-35, -6,  3),(-75,-35,-20, -6),(-73,-42,-33,-20),
 (-73,-58,-42,-33),(-75,-65,-53,-42),
 # Europe
 (-10,  3, 36, 44),( -5, 16, 43, 51),( -2, 20, 47, 55),(-10,  2, 50, 59),
 (  5, 31, 55, 71),( 15, 40, 44, 60),( 12, 30, 36, 47),( 20, 60, 45, 62),
 # Africa
 (-17, 33, 15, 33),(-17, 20,  5, 15),(  8, 32,-10, 15),( 12, 41,-18,  0),
 ( 14, 36,-28,-18),( 16, 33,-35,-28),( 33, 52,  3, 13),( 43, 51,-26,-11),
 # Middle East and Central Asia
 ( 33, 60, 12, 32),( 35, 58, 13, 30),( 44, 64, 25, 42),( 48, 88, 36, 52),
 # Russia and northern Asia
 ( 28, 60, 50, 70),( 60,110, 50, 73),(110,180, 55, 72),(100,145, 45, 58),
 # South and East Asia
 ( 68, 90,  8, 32),( 88, 98, 20, 30),( 75,122, 22, 45),( 95,110,  9, 23),
 (117,126,  6, 19),(130,146, 31, 45),(126,130, 34, 43),
 # island south-east Asia and Oceania
 ( 95,120, -8,  6),(114,141,-10,  1),(131,150,-10, -1),
 (113,153,-39,-11),(166,179,-47,-34),
]
COLS,ROWS = 108,46
LAT0,LAT1 = 80.0,-58.0
VBH = ROWS/COLS*100.0            # square cells

def _xy(lon,lat):
    return ((lon+180.0)/360.0*100.0, (LAT0-lat)/(LAT0-LAT1)*VBH)

def worldmap(pins):
    """pins: (lon, lat, label, strength, placement). placement: above|below|left|right."""
    dots=[]
    for r in range(ROWS):
        lat=LAT0-(r+0.5)/ROWS*(LAT0-LAT1)
        for c in range(COLS):
            lon=-180.0+(c+0.5)/COLS*360.0
            if any(a<=lon<=b and y0<=lat<=y1 for a,b,y0,y1 in _BOX):
                x,y=_xy(lon,lat)
                dots.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.30"/>')
    pinsvg=''
    for lon,lat,lab,st,place in pins:
        x,y=_xy(lon,lat)
        if place=='above':   lx,ly,anch = x, y-2.6, 'middle'
        elif place=='below': lx,ly,anch = x, y+3.9, 'middle'
        elif place=='left':  lx,ly,anch = x-2.6, y+0.62, 'end'
        else:                lx,ly,anch = x+2.6, y+0.62, 'start'
        pinsvg+=(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.9" class="halo p-{st}"/>'
                 f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.05" class="pin p-{st}"/>'
                 f'<text x="{lx:.2f}" y="{ly:.2f}" class="pinlab" text-anchor="{anch}">{lab}</text>')
    return (f'<div class="mapwrap"><svg viewBox="-3 -3 106 {VBH+6:.1f}" '
            f'preserveAspectRatio="xMidYMid meet" class="worldsvg">'
            f'<g class="wd">{"".join(dots)}</g>{pinsvg}</svg></div>')
