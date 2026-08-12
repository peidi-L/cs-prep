"""Command-line FizzBuzz practice."""

from __future__ import annotations

import sys


def fizz_buzz(limit: int) -> list[str]:
    result = []

    for number in range(1, limit + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))

    return result


def parse_limit(args: list[str]) -> int:
    if len(args) != 2:
        raise ValueError("Usage: python fizz_buzz.py LIMIT")

    limit = int(args[1])
    if limit < 1:
        raise ValueError("LIMIT must be at least 1")

    return limit


def main() -> None:
    try:
        limit = parse_limit(sys.argv)
    except ValueError as error:
        print(error)
        raise SystemExit(1)

    for item in fizz_buzz(limit):
        print(item)


if __name__ == "__main__":
    main()
