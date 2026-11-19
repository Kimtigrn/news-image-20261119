# The World in One Day — 19 November 2026

An entry for the [make.fun bounty "Sum up 19 November's world news in one
image"](https://make.fun/bounty/news-image-20261119) ($250, 50 paid places).

## What it is

A single Python script, `main.py`, draws a one-page newspaper poster
(1024×1024 PNG) summing up Thursday 19 November 2026 in six stories:

1. **GTA VI launches worldwide** — Rockstar's sequel unlocks at midnight
   around the globe, New Zealand first, with pre-orders past $1.5 billion.
2. **Trump, Xi and Putin meet in Shenzhen** — the first trilateral of the
   three leaders, with nuclear arms control on the table.
3. **Anthropic's shares start trading** — the Claude maker lists on Nasdaq
   as ANT, priced at $83 in a record $81bn offering.
4. **Voyager 1 is one light-day from Earth** — NASA confirms the 1977 probe
   has crossed 16 billion miles.
5. **Cyclone Akvan nears India's east coast** — red alert for coastal
   Andhra Pradesh and south Odisha, landfall expected Friday.
6. **Kuwait repels the first Iranian attack in two months** — air defences
   down drones aimed at a US base; Bahrain intercepts attacks too.

Every fact above was checked against a source dated 19 November 2026
(Reuters, AP, NASA, IMD, BBC, Bloomberg). Nothing is invented: the script
carries no news feed and makes no network calls.

## How to run it

```sh
python3 main.py
```

This writes `entry.png` next to the script. Requirements: Python 3.12+
and Pillow (`pip install pillow`). The poster is fully deterministic —
running it twice produces byte-identical output, because the skyline
artwork uses a fixed random seed and every story is baked into the code.
Verify that yourself with:

```sh
python3 main.py && sha256sum entry.png
python3 main.py && sha256sum entry.png   # same hash both times
```

## How it is drawn

The page is laid out like a front page: a serif masthead with the date in
red, the GTA VI launch as the lead story beside a hand-drawn sunset
skyline of Vice City (gradient bands, a low sun, tower silhouettes with
lit windows), then a three-column row (Shenzhen, Anthropic, Voyager 1)
and a two-column row (Cyclone Akvan, Kuwait), each with a small icon
drawn from Pillow primitives — flags, a rising bar chart, a satellite,
a cyclone swirl, a shield. All text is wrapped to its column by measuring
with the actual font, so nothing overlaps and nothing is cut off.

## Files

- `main.py` — the poster renderer (stdlib + Pillow only)
- `entry.png` — the rendered poster (1024×1024)
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
