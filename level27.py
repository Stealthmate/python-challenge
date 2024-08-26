# http://www.pythonchallenge.com/pc/hex/speedboat.html

# did you say gif?
# OK, obviously change the image link to gif. That's how we get zigzag.gif

# boat. row.
# row...? Rows of the image?

# Zig zag the rows of the image?

# hint: something about bz2. Please don't tell me...
# Ah I forgot to inspect the GIF palette.


import bz2

import numpy as np
from PIL import Image

im = Image.open("level27/zigzag.gif")
data = np.array(im.getdata())
print(im.n_frames)
print(im.size)
palette = im.getpalette()[::3]
print(palette)

translated_data = list()

for x in data:
    translated_data.append(palette[x])

zipped = list(zip(data[1:], translated_data[:-1]))
diff = list(filter(lambda p: p[0] != p[1], zipped))

bz2_data = bytes([x[0] for x in diff])
decomp = bz2.decompress(bz2_data).decode()

import keyword

print(
    [
        x
        for x in decomp.split(" ")
        if (not keyword.iskeyword(x)) and x not in ["exec", "print"]
    ]
)

# repeat switch

# http://www.pythonchallenge.com/pc/ring/bell.html
# repeat
# switch

# OK, I basically copied the code from the hint above. But now the question is - how dafuq do you even reach the answer??

# Translation using the GIF palette seems possible enough. But then why zip the translated data with the original?
# Why the 1: and :-1 offsets?
# Why pick only the pairs which are different?

# The zig-zaggy part on the speedboat image maybe kinda suggests taking the 1: and :-1 offsets, although that's quite the stretch.
# <head> says "between the tables"
# Does this mean "zig-zag between the tables?"
