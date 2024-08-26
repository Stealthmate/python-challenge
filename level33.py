# http://www.pythonchallenge.com/pc/rock/beer.html

# beer2.png

# remove its power... log?

# yeah, I ended up basically copying the hint again.
# Hunch about reducing high values was kinda right I guess, but
# no way I could have thought about looking at the histogram and shit.

import time

import numpy as np
from PIL import Image

im = Image.open("level33/beer2.png")
data = np.array(im.getdata()).astype("uint8")

for i in range(33):
    data = data.flatten()
    m = np.max(data)
    data = data[data < m - 1]
    print(len(data), m, data.dtype)
    l = int(np.sqrt(len(data)))
    im2 = Image.fromarray(data.reshape((l, l)), mode="L")
    im2.show()
    time.sleep(0.2)

# http://www.pythonchallenge.com/pc/rock/gremlins.html
