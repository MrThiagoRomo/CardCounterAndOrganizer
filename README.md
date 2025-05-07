# MTG Card Count Utility

A lightweight Python script that scans multiple deck‑list *.txt* files, tallies each **Magic: The Gathering** card name it finds, and writes a neatly‑sorted summary to a single text file.

---

## Features

* **Batch scan** every `*.txt` file in the working directory.
* **Smart parsing** strips leading quantities such as `4 Lightning Bolt` or `2x Thoughtseize`.
* **Case‑insensitive tally** so `Lightning Bolt` and `lightning bolt` are merged.
* **Custom threshold**: keep only cards that appear at least *n* times (default **10**).
* **Flexible output**: choose any filename and path for the results.
* **Minimal console output**: after it runs, you see only the result file’s name and full path.

---

## Requirements

* **Python ≥ 3.8** (script uses only the standard library).

> **Tip:** On Windows, use *python* in commands; on macOS / Linux it may be *python3*.

---

## Installation

Clone or download this repository, then place your deck‑list text files in the same folder as **`mtg_count_to_file.py`**.

```bash
# clone with git (optional)
$ git clone https://github.com/your‑handle/mtg‑card‑count.git
$ cd mtg‑card‑count
```

No extra packages are needed.

---

## Usage

```bash
# Basic run – counts each card across all *.txt files and
# writes cards with ≥10 copies to card_counts.txt
$ python mtg_count_to_file.py
```

### Command‑line options

| Option     | Short | Default           | Description                                     |
| ---------- | ----- | ----------------- | ----------------------------------------------- |
| `--output` | `-o`  | `card_counts.txt` | Path / name for the results file.               |
| `--min`    | `-m`  | `10`              | Only include cards with **≥ MIN** total copies. |

### Examples

```bash
# Save results to a custom file
$ python mtg_count_to_file.py -o totals.txt

# Keep cards that appear 15 times or more
$ python mtg_count_to_file.py -m 15

# Combine both flags
$ python mtg_count_to_file.py -m 20 -o high_volume_cards.txt
```

After the script finishes, you’ll see output similar to:

```
✔ Results written to "card_counts.txt"
  Location: /Users/alex/decks/card_counts.txt
```

Open that file to view the list:

```
# MTG card totals (≥ 10 copies) written on 2025‑05‑07 14:30

 24  Lightning Bolt
 17  Thoughtseize
 11  Ponder
```

---

## Customizing parsing rules

Deck‑list formats vary. If you need to support different quantity prefixes (e.g. `4x`, `SB:` for sideboard lines, etc.) edit the **`CARD_LINE_RE`** regular expression near the top of the script.

---

## Troubleshooting

| Symptom                           | Fix                                                                                                                                      |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **No cards appear in the output** | Ensure your text files are in the same directory as the script and that each line contains a quantity + card name or just the card name. |
| **UnicodeDecodeError**            | Confirm your decklists are saved with UTF‑8 encoding.                                                                                    |

---

## Contributing

1. Fork the repo, create a branch (`git checkout -b feature/foo`).
2. Commit your changes with clear messages.
3. Push to the branch and open a Pull Request.

---

## License

MIT © 2025 Your Name.

Feel free to use, modify, and distribute – but no warranty is provided.

---

## Acknowledgements

* Inspired by countless MTG community deck‑sharing formats.
* Uses Python’s `argparse`, `pathlib`, and `collections.Counter` under the hood.

Happy brewing and may your topdecks be ever in your favour!
