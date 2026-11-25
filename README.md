# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/itzalisha99/3-am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/itzalisha99/3-am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

A hardware wallet refuses to sign a transaction at 3 AM — because it has
checked its human's transaction history, and at 3 AM the human only ever
buys the top. So tonight, it declines.

## Entry

> I checked your transaction history. At 3 AM you only ever buy the top. Declined.

(80 characters, one line.)

## How it works

`main.py` (Python standard library only) writes the excuse to
`/output/entry.txt` after checking it against the bounty gate: 1–200
characters, UTF-8, not only whitespace, a single line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
