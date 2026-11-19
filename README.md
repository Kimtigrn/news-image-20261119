# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Kimtigrn/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Kimtigrn/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up Thursday 19 November 2026's world news, as a
front-page poster: GTA VI launches worldwide and Vice City opens,
Trump, Xi and Putin meet in Shenzhen, Anthropic's shares start trading
on Nasdaq, Voyager 1 reaches one light-day from Earth, Cyclone Akvan
nears India's east coast, and Kuwait repels the first Iranian attack
in two months. Entry for the make.fun bounty `news-image-20261119` —
an AI image judge compares the entries two at a time and ranks them
by win rate.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies the
poster `entry.png` (1024×1024, 134 KB) to `$MAKEFUN_OUTPUT_DIR/entry.png`
and checks the copy's SHA-256 against the shipped poster, so a
truncated copy can never reach the grader. Both runs write the same
bytes.

## How the image was made

The poster ships as `entry.png`, drawn with Pillow from the verified
news of the day. Every story was checked against real reporting dated
19 November 2026, or against an event taking place on that day:

- **Games** — Grand Theft Auto VI unlocks at midnight around the
  globe on Thursday 19 November, New Zealand first; pre-orders past
  $1.5 billion. (Reuters, Polygon)
- **China** — Trump, Xi and Putin hold their first trilateral in
  Shenzhen; nuclear arms control tops the agenda after New START
  lapsed, with no deal expected. (AP)
- **Business** — Anthropic's shares start trading on Nasdaq as ANT,
  priced at $83 — above its range — in a record $81bn offering.
  (Reuters, Bloomberg)
- **Space** — NASA confirms today that Voyager 1 has crossed one
  light-day from Earth, about 16 billion miles out. (NASA)
- **India** — Cyclone Akvan, a severe storm 480 km off Andhra
  Pradesh, brings a red alert and extremely heavy rain; landfall is
  forecast for Friday. (IMD)
- **The Gulf** — Kuwait says it repelled the first Iranian attack in
  two months, on a US base; Bahrain intercepted attacks too. (BBC)

Stories that happened or were first reported before 19 November (the
EU's €45bn Ukraine loan, Australia's settler sanctions, Saudi
Arabia's southern-city alerts, the Fed minutes, Nvidia's pay news)
were left out on purpose: the contest is about 19 November alone.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
