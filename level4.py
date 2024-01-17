import re

import requests

PATTERN = r"and the next nothing is (.+)"

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
# tag = '12345'
# tag = '94485'
# tag = str(16044 // 2)
tag = "66831"

response = requests.get(URL.format(tag), timeout=1000).text
match = re.search(PATTERN, response)
while match:
    tag = match.group(1)
    response = requests.get(URL.format(tag), timeout=1000).text
    print(response)
    match = re.search(PATTERN, response)
    print(match)
print(response)

target = "peak"
print(f"http://www.pythonchallenge.com/pc/def/{target}.html")
