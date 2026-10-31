# The Last Lighthouse

A story-driven Python signal-decoding adventure. A storm has cut the coast off from the world. You are the last lighthouse keeper. Decode five transmissions and bring the beacon back online.

## Features
- Five connected story chapters.
- Morse code, binary ASCII, hexadecimal ASCII, and Caesar cipher puzzles.
- Hints, streak-based scoring, and a saved personal best.
- Short field notes explain the computing idea behind each signal.
- No third-party packages.

## Requirements
Python 3.10+

## Run
```bash
python main.py
```

## Tests
```bash
python -m unittest discover -s tests -v
```

## Concepts
| Concept | What you practise |
|---|---|
| Morse code | Dots, dashes, and word separators |
| Binary | Reading groups of 0s and 1s |
| ASCII | Mapping numeric codes to characters |
| Hexadecimal | Reading byte values in base 16 |
| Caesar cipher | A simple substitution cipher |

## Project layout
```text
LastLighthouse/
├── main.py
├── lighthouse/
│   ├── __init__.py
│   ├── engine.py
│   └── game.py
├── tests/
│   └── test_engine.py
├── README.md
├── LICENSE
└── .gitignore
```
Your best score is stored in `lighthouse_save.json` after completing the campaign. Delete it to reset the record.
