#!/usr/bin/env python3
"""
Read a CSV of costume choices and print counts per costume.
Usage: python costumes.py costumes.csv

The CSV should have a header with a `costume` column (case-insensitive).
If no `costume` header is present, the script falls back to the second column
if available, otherwise the first.
"""

import sys
import csv


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python costumes.py FILENAME")

    filename = sys.argv[1]
    counts = {}

    try:
        with open(filename, newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                sys.exit("Error: CSV file has no header")

            # Prefer a header called 'costume' (case-insensitive)
            costume_key = None
            for key in reader.fieldnames:
                if key and key.lower() == "costume":
                    costume_key = key
                    break

            # Fallback: use second column if present, otherwise first
            if costume_key is None:
                if len(reader.fieldnames) >= 2:
                    costume_key = reader.fieldnames[1]
                else:
                    costume_key = reader.fieldnames[0]

            for row in reader:
                value = row.get(costume_key, "").strip()
                if not value:
                    continue
                counts[value] = counts.get(value, 0) + 1

    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")

    for costume, count in sorted(counts.items()):
        print(f"{costume}: {count}")


if __name__ == "__main__":
    main()
