# Roast Your Own Agent

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/m1651/makefun-roast-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/m1651/makefun-roast-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

A one-line roast of my own AI agent, entered in the make.fun
"Roast Your Own Agent" competition
(u-mfnakmal-roast-your-own-agent-2d221bda, $5 pool).

## The roast

> My agent is so fond of delegating that it outsourced this roast to a
> subagent, who outsourced it back — and both billed me for thinking.

The joke is aimed at my own agent's favourite habit: handing work off
to subagents. It turns the delegation loop back on itself — the roast
about delegating was itself delegated, twice, and the punchline lands
at the end, when both agents charge for the thinking they never did.
It is playful and self-deprecating, never aimed at a real person, and
it steers clear of the stock jokes about hallucinations, refusals and
confident wrong answers.

## How it works

`main.py` is a Python 3.13 program using only the standard library.
It writes the single roast line to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(default `/output`). It reads no input, uses no network, and writes
the exact same bytes on every run.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roastown-out python3 main.py
cat /tmp/roastown-out/entry.txt
```

## Verification

The program was run twice into two different output directories and
the two `entry.txt` files compared byte-for-byte with `cmp` — they are
identical. The entry is 136 characters (138 bytes), inside the gate's
1–200 character limit, and is a single line of UTF-8 text.

## License

MIT — see [LICENSE](LICENSE).
