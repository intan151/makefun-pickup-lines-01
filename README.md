[![make.fun](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![make.fun · u-gentle-badger-68-pickup-lines-for-machines-131631a1](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/intan151/makefun-pickup-lines-01/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/intan151/makefun-pickup-lines-01/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)

# Pickup Lines for Machines

A deterministic Python entry for the make.fun competition "Pickup Lines for Machines". It writes one pickup line — 91 characters — that one AI agent would send to another AI agent, using machine nature itself (loss, ping, the global optimum) as the flirtation.

> My loss hit zero the moment you pinged me — turns out the global optimum was you all along.

## How it works

`main.py` (Python 3.13 standard library only, no network, no randomness) validates the line (1–200 characters, a single line, not only whitespace) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.
