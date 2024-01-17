# http://www.pythonchallenge.com/pc/def/equality.html
import re

PATTERN = re.compile(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")

text = ""
with open("level3.txt") as f:
    text = f.read()

results = re.findall(PATTERN, text)
target = "".join(results)

print(f"http://www.pythonchallenge.com/pc/def/{target}.html")
