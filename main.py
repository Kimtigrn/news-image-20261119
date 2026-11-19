#!/usr/bin/env python3
"""Render a one-page newspaper poster summing up 19 November 2026.

Reads nothing at runtime: every story is baked into STORIES below, so the
program is deterministic and needs no network. Output is a 1024x1024 PNG.

Run:  python3 main.py            (writes entry.png to $MAKEFUN_OUTPUT_DIR,
                                  or next to this file when unset)
"""

import hashlib
import os
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
# The grader mounts the repo read-only at /bot and gives a writable
# $MAKEFUN_OUTPUT_DIR (/output); writing next to main.py fails there.
# Locally the variable is unset, so the poster still lands next to main.py.
OUT = os.path.join(
    os.environ.get(
        "MAKEFUN_OUTPUT_DIR",
        os.path.dirname(os.path.abspath(__file__)),
    ),
    "entry.png",
)

PAPER = (247, 243, 232)
INK = (24, 22, 20)
RED = (163, 22, 33)
GREY = (96, 90, 80)
RULE = (40, 36, 32)
SKY_TOP = (238, 120, 150)
SKY_MID = (244, 140, 82)
SKY_LOW = (250, 196, 110)
SUN = (252, 222, 130)
TOWER = (38, 28, 66)
WINDOW_LIT = (255, 214, 110)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def serif_b(size):
    return font("DejaVuSerif-Bold.ttf", size)


def serif(size):
    return font("DejaVuSerif.ttf", size)


def sans_b(size):
    return font("DejaVuSans-Bold.ttf", size)


def sans(size):
    return font("DejaVuSans.ttf", size)


def wrap(text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit inside max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(draw, x, y, max_w, lines, fnt, fill=INK, leading=None):
    """Draw stacked lines; returns the y just below the last line."""
    step = leading if leading is not None else int(fnt.size * 1.28)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def kicker(draw, x, y, label, fnt):
    draw.text((x, y), label, font=fnt, fill=RED)
    return y + int(fnt.size * 1.5)


def hrule(draw, x0, x1, y, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def skyline_panel(draw, x, y, w, h):
    """Sunset skyline over Vice City, drawn from primitive shapes."""
    # Horizontal sunset bands, top to bottom.
    bands = [SKY_TOP, (240, 128, 116), SKY_MID, (248, 172, 96), SKY_LOW]
    bh = h // len(bands)
    for i, colour in enumerate(bands):
        draw.rectangle([x, y + i * bh, x + w, y + (i + 1) * bh], fill=colour)
    # Low sun, half-hidden behind the towers.
    cx, cy, r = x + int(w * 0.62), y + int(h * 0.62), int(w * 0.13)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SUN)
    # Tower silhouettes with lit windows; seeded so the art never changes.
    rng = random.Random(19112026)
    cursor = x
    while cursor < x + w - 18:
        tw = rng.randint(26, 52)
        th = rng.randint(int(h * 0.28), int(h * 0.62))
        top = y + h - th
        draw.rectangle([cursor, top, cursor + tw, y + h], fill=TOWER)
        for wy in range(top + 8, y + h - 6, 13):
            for wx in range(cursor + 5, cursor + tw - 5, 11):
                if rng.random() < 0.45:
                    draw.rectangle([wx, wy, wx + 4, wy + 6], fill=WINDOW_LIT)
        cursor += tw + rng.randint(2, 8)
    # Ground strip.
    draw.rectangle([x, y + h - 8, x + w, y + h], fill=(20, 14, 40))
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    # "VICE CITY" pill badge.
    label = "VICE CITY"
    lf = sans_b(22)
    lw = int(lf.getlength(label)) + 30
    bx = x + (w - lw) // 2
    by = y + 16
    draw.rounded_rectangle([bx, by, bx + lw, by + 38], radius=8, fill=(30, 18, 58))
    draw.text((bx + 15, by + 7), label, font=lf, fill=(255, 120, 190))


def flag_trio(draw, x, y):
    """Three tiny meeting flags on poles."""
    colours = [(178, 34, 34), (200, 40, 40), (30, 60, 140)]
    for i, c in enumerate(colours):
        px = x + i * 26
        draw.line([(px, y), (px, y + 34)], fill=INK, width=2)
        draw.rectangle([px, y, px + 20, y + 13], fill=c)


def chart_icon(draw, x, y):
    """Rising bar chart with an arrow."""
    heights = [10, 18, 14, 26, 34]
    for i, hh in enumerate(heights):
        bx = x + i * 13
        draw.rectangle([bx, y + 36 - hh, bx + 8, y + 36], fill=(30, 90, 160))
    draw.line([(x - 2, y + 2), (x + 66, y - 6)], fill=RED, width=3)
    draw.polygon([(x + 66, y - 6), (x + 56, y - 4), (x + 62, y + 4)], fill=RED)


def satellite_icon(draw, x, y):
    """A small satellite: body, two panels, dish."""
    draw.rectangle([x + 18, y + 12, x + 38, y + 28], fill=(60, 70, 90))
    draw.rectangle([x, y + 16, x + 16, y + 24], fill=(40, 90, 160))
    draw.rectangle([x + 40, y + 16, x + 56, y + 24], fill=(40, 90, 160))
    draw.line([(x + 38, y + 12), (x + 50, y + 2)], fill=INK, width=2)
    draw.ellipse([x + 48, y, x + 56, y + 8], outline=INK, width=2)


def spiral_icon(draw, x, y):
    """Cyclone swirl: concentric arcs."""
    for r, start in [(26, 20), (19, 140), (12, 260)]:
        draw.arc([x - r, y - r, x + r, y + r], start, start + 230,
                 fill=(30, 90, 160), width=4)
    draw.ellipse([x - 4, y - 4, x + 4, y + 4], fill=RED)


def shield_icon(draw, x, y):
    """Shield with a check mark (defences held)."""
    draw.polygon([(x + 18, y), (x + 38, y + 6), (x + 38, y + 22),
                  (x + 18, y + 38), (x - 2, y + 22), (x - 2, y + 6)],
                 fill=(30, 110, 70))
    draw.line([(x + 7, y + 18), (x + 15, y + 26), (x + 30, y + 10)],
              fill=(255, 255, 255), width=4)


STORIES = {
    "lead": {
        "kicker": "GAMES  \u00b7  GRAND THEFT AUTO VI",
        "headline": "Vice City opens: GTA VI launches worldwide",
        "body": ("After 13 years, Rockstar's sequel unlocks at midnight "
                 "around the globe \u2014 New Zealand first \u2014 with "
                 "pre-orders past $1.5 billion."),
        "caption": "Vice City at dusk \u2014 13 years in the making.",
    },
    "china": {
        "kicker": "CHINA  \u00b7  DIPLOMACY",
        "headline": "Trump, Xi and Putin meet in Shenzhen",
        "body": ("The first trilateral of the three nuclear powers: arms "
                 "control on the table after New START lapsed; no deal is "
                 "expected."),
        "icon": flag_trio,
    },
    "business": {
        "kicker": "BUSINESS  \u00b7  MARKETS",
        "headline": "Anthropic's shares start trading today",
        "body": ("The AI maker behind Claude lists on Nasdaq as ANT, "
                 "priced at $83 \u2014 above its range \u2014 in a record "
                 "$81bn offering."),
        "icon": chart_icon,
    },
    "space": {
        "kicker": "SPACE",
        "headline": "Voyager 1 is one light-day from Earth",
        "body": ("NASA confirms today: the 1977 probe has crossed 16 "
                 "billion miles; a radio signal now takes a full day each "
                 "way."),
        "icon": satellite_icon,
    },
    "india": {
        "kicker": "INDIA  \u00b7  WEATHER",
        "headline": "Cyclone Akvan nears India's east coast",
        "body": ("Red alert as the severe storm closes to 480 km off "
                 "Andhra Pradesh; extremely heavy rain today, landfall "
                 "Friday."),
        "icon": spiral_icon,
    },
    "gulf": {
        "kicker": "THE GULF",
        "headline": "Kuwait repels first Iranian attack in two months",
        "body": ("Kuwait's air defences down drones aimed at a US base; "
                 "Bahrain intercepts attacks too, after the US hit Qeshm "
                 "Island."),
        "icon": shield_icon,
    },
}


def story_column(draw, x, y, w, story, head_size, body_size):
    """Kicker + headline + body for one story; returns bottom y."""
    y = kicker(draw, x, y, story["kicker"], sans_b(17))
    y = block(draw, x, y, w, wrap(story["headline"], serif_b(head_size), w),
              serif_b(head_size), leading=int(head_size * 1.18))
    y += 6
    y = block(draw, x, y + 2, w, wrap(story["body"], sans(body_size), w),
              sans(body_size), leading=int(body_size * 1.32))
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Double frame around the whole page.
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)
    d.rectangle([18, 18, W - 19, H - 19], outline=INK, width=1)

    # --- Masthead -------------------------------------------------------
    title = "THE WORLD IN ONE DAY"
    tf = serif_b(62)
    d.text(((W - tf.getlength(title)) / 2, 34), title, font=tf, fill=INK)
    hrule(d, 44, W - 44, 118, width=3)
    date = "THURSDAY,  19  NOVEMBER  2026"
    df = sans_b(30)
    d.text(((W - df.getlength(date)) / 2, 130), date, font=df, fill=RED)
    tag = "SIX STORIES THAT DEFINED THE DAY  \u00b7  FROM THE WORLD'S NEWS WIRES"
    tg = sans(17)
    d.text(((W - tg.getlength(tag)) / 2, 172), tag, font=tg, fill=GREY)
    hrule(d, 44, W - 44, 202, width=2)

    # --- Lead story + skyline -------------------------------------------
    lead = STORIES["lead"]
    lx, ly, lw = 44, 224, 540
    ly = kicker(d, lx, ly, lead["kicker"], sans_b(19))
    ly = block(d, lx, ly, lw,
               wrap(lead["headline"], serif_b(42), lw), serif_b(42),
               leading=50)
    ly += 8
    ly = block(d, lx, ly + 4, lw,
               wrap(lead["body"], sans(20), lw), sans(20), leading=27)

    px, py, pw, ph = 612, 224, 368, 216
    skyline_panel(d, px, py, pw, ph)
    cap = sans(15)
    d.text((px, py + ph + 10), lead["caption"], font=cap, fill=GREY)
    hrule(d, 44, W - 44, 512, width=2)

    # --- Middle row: three stories --------------------------------------
    col_w, gap = 296, 24
    y0 = 534
    for i, key in enumerate(("china", "business", "space")):
        cx = 44 + i * (col_w + gap)
        story = STORIES[key]
        story["icon"](d, cx + col_w - 76, y0 - 4)
        story_column(d, cx, y0, col_w, story, 26, 17)
        if i < 2:
            d.line([(cx + col_w + 12, y0), (cx + col_w + 12, y0 + 210)],
                   fill=(200, 192, 172), width=1)
    hrule(d, 44, W - 44, 764, width=1, fill=(200, 192, 172))

    # --- Bottom row: two stories ----------------------------------------
    y1 = 786
    for i, key in enumerate(("india", "gulf")):
        cx = 44 + i * 490
        story = STORIES[key]
        story["icon"](d, cx + 420, y1 - 2)
        story_column(d, cx, y1, 400, story, 26, 17)
        if i == 0:
            d.line([(cx + 440, y1), (cx + 440, y1 + 160)],
                   fill=(200, 192, 172), width=1)

    # --- Footer ---------------------------------------------------------
    hrule(d, 44, W - 44, 962, width=2)
    foot = ("As reported on 19 November 2026 by  Reuters  \u00b7  AP  "
            "\u00b7  NASA  \u00b7  IMD  \u00b7  BBC  \u00b7  Bloomberg")
    ff = sans(16)
    d.text(((W - ff.getlength(foot)) / 2, 972), foot, font=ff, fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    digest = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    print(f"Wrote {OUT}  {os.path.getsize(OUT)} bytes  sha256={digest}")


if __name__ == "__main__":
    main()
