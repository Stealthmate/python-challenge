# https://www.pythonchallenge.com/pc/hex/decent.html
# > you've got his email
# > apologize
# is this about mozart again?

# turns out I did have his email - leopold.moz@pythonchallenge.com
# ref: http://www.pythonchallenge.com/pc/hex/bin.html

# > Never mind that.
# > Have you found my broken zip?
# > md5: bbb8b499a0eef99b52c7f13f4e78c24b
# > Can you believe what one mistake can lead to?

# OK, so the ZIP from level24 has the hash:
# > md5: bbf6616928e23ecfef4b717f281c53cc
# Now what am I supposed to do...

# Unzipping yields mybroken.gif
# > md5: 6494c6fbca209100f0c956a666130c86

# Saw the hint. Apparently I'm supposed to brute-force hack the broken zip to match the hash.
# oh my god...

import hashlib

content = None
with open("level24/mybroken.zip", mode="rb") as f:
    content = f.read()

for i in range(len(content)):
    print(i)
    for x in range(255):
        mod_content = list(content)
        mod_content[i] = x
        h = hashlib.md5(bytes(mod_content)).hexdigest()
        # print(h)
        if h == "bbb8b499a0eef99b52c7f13f4e78c24b":
            content = mod_content
            break

with open("level26/mybroken-fixed.zip", mode="wb") as f:
    f.write(bytes(content))

# speed
# http://www.pythonchallenge.com/pc/hex/speed.html did not work
# ...
# speedboat?
# yay!
# http://www.pythonchallenge.com/pc/hex/speedboat.html
