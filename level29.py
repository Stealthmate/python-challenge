# http://www.pythonchallenge.com/pc/ring/guido.html

# silence!
# whoisit.jpg
# tweety from looney tunes
# glass, glasses, kinda looks like a gas mask? or a professor? With big nose?

# knock-knock joke?

# hint: silent empty lines in HTML.
# Dammit, should have noticed this myself...

import bz2

lines = []
with open("./level29/lines.txt") as f:
    for line in f:
        lines.append(len(list(x for x in line if x == " ")))

lines = bytes(lines)

print(lines)

# Starts with BZ. Time for bz2 I guess

dc = bz2.BZ2Decompressor()
data = dc.decompress(bytes(lines), max_length=100)
print(data)

# Isn't it clear? I am yankeedoodle!
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

# wow, this was surprisingly easy?
