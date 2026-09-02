#!/usr/bin/env python3
"""sources/media/*.png -> deck/assets.py  (base64 data URIs)

The deck ships as ONE self-contained HTML file, so every image has to travel inside it.
This trims transparent margins, resizes to about 2x the display size, and writes each
image out as a `data:image/png;base64,...` constant.

Why regenerate rather than hand-edit: `deck/assets.py` is derived, and the rule in
CLAUDE.md is that anything derived must be reproducible by a script in tools/. The
originals in sources/media/ are the evidence and are never edited.

Nominative use only. Every logo here identifies the company being discussed, at the
point it is discussed. Nothing in the deck is styled to imply Braze produced it, and
the title slide's mark is Braze's wordmark on a plate captioned as the subject of the
analysis, not as its author.

Usage:  python3 tools/build_assets.py
"""
import base64
import io
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "sources", "media")
OUT = os.path.join(REPO, "deck", "assets.py")

# Braze publishes exactly one wordmark file and it is black on transparent, which on this
# deck's near-black ground can only be shown on a white plate - and a white plate is the
# brightest object on the slide, louder than the title it sits above. So the mark is
# recoloured, and the colour is not invented: #BC6BF2 is Braze's own light violet, read
# off the inline CSS of braze.com. Their darker brand violet, #4411D6, is unreadable on
# #141821 at about 1.9:1. OfferFit's black wordmark is knocked out to white for the same
# reason, its coloured glyph left alone. Both alterations are recorded in
# sources/media/PROVENANCE.md; the originals in sources/ are untouched.
BRAZE_VIOLET = (0xBC, 0x6B, 0xF2)


def strip_white(im, thresh=246):
    """Make a near-white background transparent.

    OfferFit's only surviving asset is an Open Graph card: 1200x600 with an OPAQUE white
    background, not a transparent logo. trim() found nothing to trim and the knockout
    turned white text onto a white field, which is how a logo disappears while every
    check still passes. Anything at or above the threshold on all three channels loses
    its alpha; the four-square glyph and the letterforms are all well below it."""
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a and r >= thresh and g >= thresh and b >= thresh:
                px[x, y] = (r, g, b, 0)
    return im


def recolour(im, rgb, only_dark=True):
    """Repaint opaque pixels, keeping the alpha channel - so the letterforms are exactly
    the letterforms Braze published, in a different ink. only_dark leaves anything already
    coloured alone, which is what keeps OfferFit's four-square glyph intact."""
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            if only_dark and max(r, g, b) > 110:
                continue
            px[x, y] = (rgb[0], rgb[1], rgb[2], a)
    return im


# (constant, filename, target width in px, format, note for the generated file)
# Logos stay PNG because they need the alpha channel; photographs go to JPEG, which is
# roughly a fifth of the size at a quality nobody can see the difference at on a slide.
ASSETS = [
    ("LOGO", "braze-logo.png", 300, "png",
     "Braze wordmark, from the site header at braze.com, recoloured to Braze's own "
     "#BC6BF2 so it sits on the dark ground with no plate behind it.", BRAZE_VIOLET),
    ("OFFERFIT", "offerfit-logo.png", 420, "png",
     "OfferFit's own logo, from the Internet Archive capture of offerfit.ai dated "
     "2024-12-31, with the black wordmark knocked out to white and the four-square "
     "glyph left in its own colours. Not on the live web: offerfit.ai now serves a "
     "Braze page titled 'BrazeAI Decisioning Studio'.", (0xF2, 0xEE, 0xE8)),
    ("CEO", "ceo-magnuson.png", 260, "jpg",
     "Bill Magnuson, from Braze's own investor-relations leadership page, where the "
     "alt text reads 'Chairman, Chief Executive Officer, President, and Cofounder'.", None),
]

# NOT ENCODED, deliberately. sources/media/founders-2011-techcrunch-disrupt.png is a real,
# properly sourced Braze-published photograph and it stays in sources/ as evidence - but it
# is not in the deck. It put a second photographic treatment on slide 7 next to a circular
# portrait, at a different width, from a low-resolution original with cropped lettering
# along its top edge. One photographic treatment per slide; see deck/COMPONENTS.md.
# Re-adding it is one line here plus one in slides_b.py, if a later pass disagrees.


def trim(im):
    """Drop fully transparent margins. A logo with 40% empty pixels renders small."""
    if im.mode != "RGBA":
        return im
    bbox = im.getchannel("A").getbbox()
    return im.crop(bbox) if bbox else im


def encode(path, width, fmt, tint=None):
    im = Image.open(path).convert("RGBA")
    if tint:
        im = strip_white(im)
        im = recolour(im, tint)
    im = trim(im)
    if im.width > width:
        h = round(im.height * width / im.width)
        im = im.resize((width, h), Image.LANCZOS)
    buf = io.BytesIO()
    if fmt == "jpg":
        # Flatten onto white: these sit on a light plate or a circular crop, so the
        # matte never shows, and JPEG has no alpha to lose.
        flat = Image.new("RGB", im.size, (255, 255, 255))
        flat.paste(im, mask=im.getchannel("A"))
        flat.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
        mime = "jpeg"
    else:
        im.save(buf, "PNG", optimize=True)
        mime = "png"
    return base64.b64encode(buf.getvalue()).decode(), im.size, len(buf.getvalue()), mime


def main():
    lines = [
        "# -*- coding: utf-8 -*-",
        '"""Generated by tools/build_assets.py — do not edit by hand.',
        "",
        "Images as base64 data URIs so deck/braze-deck.html stays a single file that can be",
        "emailed, opened offline and printed without fetching anything. Originals and their",
        "provenance are in sources/media/.",
        '"""',
        "",
    ]
    total = 0
    for const, fname, width, fmt, note, tint in ASSETS:
        path = os.path.join(SRC, fname)
        if not os.path.exists(path):
            print("MISSING %s — %s not written" % (fname, const))
            continue
        b64, size, nbytes, mime = encode(path, width, fmt, tint)
        total += nbytes
        lines.append("# %s" % note.replace(". ", ".\n# "))
        lines.append("# %s -> %dx%d %s, %.0f KB" % (fname, size[0], size[1], mime, nbytes / 1024))
        lines.append('%s = "data:image/%s;base64,%s"' % (const, mime, b64))
        lines.append("")
        print("%-10s %-38s %4dx%-4d %6.0f KB" % (const, fname, size[0], size[1], nbytes / 1024))

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("wrote deck/assets.py — %d images, %.0f KB of PNG before base64" % (len(ASSETS), total / 1024))


if __name__ == "__main__":
    main()
