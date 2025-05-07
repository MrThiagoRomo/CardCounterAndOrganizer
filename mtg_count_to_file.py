#!/usr/bin/env python3
"""
Count repeated MTG card names across all *.txt files in the current directory
and write the results—sorted by frequency—to an output file (default:
card_counts.txt).  Only card names whose total count is ≥ 10 (or the value
you pass with -m/--min) are saved.

Usage
-----
$ python mtg_count_to_file.py                 # output to card_counts.txt
$ python mtg_count_to_file.py -o totals.txt   # custom file name
$ python mtg_count_to_file.py -m 15           # different minimum threshold
"""

from collections import Counter
from pathlib import Path
import argparse
import re
from datetime import datetime

CARD_LINE_RE = re.compile(r'^\s*(\d+\s*x?\s*)?', re.I)

def collect_card_counts(folder: Path = Path('.')) -> Counter:
    counts = Counter()
    display_case = {}          

    for txt in folder.glob('*.txt'):
        with txt.open(encoding='utf-8') as fh:
            for raw in fh:
                name = CARD_LINE_RE.sub('', raw).strip()
                if not name:
                    continue
                key = name.lower()
                counts[key] += 1
                display_case.setdefault(key, name)

    return Counter({display_case[k]: v for k, v in counts.items()})

def write_counts(counts: Counter, outfile: Path, min_total: int) -> None:
    """Write card counts ≥ min_total to *outfile*."""
    with outfile.open('w', encoding='utf-8') as fh:
        now = datetime.now().strftime('%Y‑%m‑%d %H:%M')
        fh.write(f'# MTG card totals (≥ {min_total} copies) written on {now}\n\n')
        for card, total in counts.most_common():
            if total < min_total:
                break
            fh.write(f'{total:>3}  {card}\n')

def main() -> None:
    parser = argparse.ArgumentParser(description='Tally MTG card names across *.txt files.')
    parser.add_argument(
        '-o', '--output', type=Path, default=Path('card_counts.txt'),
        help='Output file path (default: card_counts.txt)'
    )
    parser.add_argument(
        '-m', '--min', dest='min_total', type=int, default=10,
        help='Only include cards with at least this many copies (default: 10)'
    )
    args = parser.parse_args()

    counts = collect_card_counts()
    write_counts(counts, args.output, args.min_total)

    print(f'✔ Results written to "{args.output.name}"')
    print(f'  Location: {args.output.resolve()}')

if __name__ == '__main__':
    main()
