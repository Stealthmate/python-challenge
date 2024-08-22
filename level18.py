# http://www.pythonchallenge.com/pc/return/balloons.html
# hint: https://www.hackingnote.com/en/python-challenge-solutions/level-18/
# oh my god you have to be fking kidding me.
# I tried "contrast", "dark", "light", "exposure".
# don't know if I'm overqualified for this, or just plain stupid...
# http://www.pythonchallenge.com/pc/return/brightness.html
# "maybe consider deltas.gz"
# I tried treating the image pixel diff as a gzip array, turns out I just had to follow the path...
# man, what the actual fuck.
# http://www.pythonchallenge.com/pc/return/deltas.gz

# I tried converting each of the left/right images back to PNG, but that didn't work.
# Then I gave up and just looked at the solution.
# I don't think I would have managed to think of this on my own.

import difflib

lines1 = []
lines2 = []

with open("level18/deltas") as f:
    for line in f:
        lines1.append(line[:53].strip())
        lines2.append(line[56:].strip())

compare = difflib.Differ().compare(lines1, lines2)

f = open("level18/f.png", "wb")
f1 = open("level18/f1.png", "wb")
f2 = open("level18/f2.png", "wb")

for line in compare:
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == "+":
        f1.write(bs)
    elif line[0] == "-":
        f2.write(bs)
    else:
        f.write(bs)

f.close()
f1.close()
f2.close()

# butter
# fly
# http://www.pythonchallenge.com/pc/hex/bin.html
