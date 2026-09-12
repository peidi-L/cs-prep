# url = input("Enter the URL: ").strip
# print(url)

# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

import re

url = input("Enter the URL: ").strip()
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: {matches.group(1)}")
