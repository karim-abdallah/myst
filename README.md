# myst 🌿

An automatic houseplant watering system — hardware prototype and MicroPython firmware. December 2019.

It ran in my apartment and a couple of friends' homes: a pump on a fixed schedule, every 4 days, three waterings on the day, two minutes each. The numbers came from experiment rather than theory, which is a polite way of saying I overwatered a basil plant to death first.

## The firmware

```
myst_sw/
├── main.py           # scheduling loop, RTC handling, entry point
├── hal.py            # pin assignment and pump on/off
├── pump.py           # timed actuation
├── connectivity.py   # WiFi association, connection state
├── initialize.py     # boot-time hardware checks
├── sensors.py        # stub — see below
└── user.py           # stub — see below
```

`hal.py` keeps the pin numbers and the pump primitives in one place, so `pump.py` never names a pin — though `main.py` still reaches for `machine` directly to get at the RTC, so the abstraction is only half-applied.

The network isn't there for remote control, it's there for the clock. On boot the device associates with WiFi and pulls time over NTP; without a network it falls back to a fixed epoch and the schedule runs blind. `connectivity.py` keeps the WLAN handle module-global so the rest of the code can ask `isConnected()` without touching the radio again — `main()` uses that to decide whether the clock can be trusted.

## What it isn't

The file list promises more than there is, so, plainly:

- `sensors.py` and `user.py` are headers with no code in them. **There is no soil-moisture sensing** — `initializeChirp()` prints a reassuring message and does nothing. Chirp was the sensor I meant to add.
- Watering is open-loop on a timer. Nothing measures the soil, and nothing stops the pump if something goes wrong.
- The scheduling arithmetic counts elapsed hours but compares them against a list of wall-clock hours; those don't line up. It watered on a workable rhythm rather than a correct one.

## Status

Prototype, 13 commits, unmaintained since 2019. Public because it kept real plants alive for months — not as a sample of finished work.
