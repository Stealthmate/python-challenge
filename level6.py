# http://www.pythonchallenge.com/pc/def/peak.html
import io
import re
import zipfile

import requests

URL = "http://www.pythonchallenge.com/pc/def/channel.zip"
data = requests.get(URL, timeout=1000).content
z = zipfile.ZipFile(io.BytesIO(data))
print(z.getinfo("46145.txt").comment)
# print(z.extractall('level6'))

PATTERN = re.compile(r"Next nothing is ([^ ]+)")

tag = "90052"
order = []
while True:
    with open(f"level6/{tag}.txt") as f:
        content = f.read()
        print(content)
        m = re.search(PATTERN, content)
        if not m:
            break
        order.append(tag)
        tag = m.groups(1)[0]

answer = "".join([z.getinfo(f"{tag}.txt").comment.decode() for tag in order])
print(answer)

# target = 'hockey'
target = "oxygen"

print(f"http://www.pythonchallenge.com/pc/def/{target}.html")
