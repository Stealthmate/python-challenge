from collections import Counter

text = ""
with open("level2.txt") as f:
    text = f.read()

count = Counter(text)
print(count.most_common()[-8:])  # equality

target = "equality"
print(f"http://www.pythonchallenge.com/pc/def/{target}.html")
