# name = input("What is your name? ").strip()
# if "," in name:
#     last, first = name.split(",", 1)

#     print(f"Hello, {first.strip()} {last.strip()}!")
# else:
#     print(f"Hello, {name}!")

import re

name = input("What is your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"Hello, {name}!")
