# http://www.pythonchallenge.com/pc/ring/grandpa.html
# FYI: grandfather rock. Yes, it looks like a dick.

# hint:
# kohsamui
# thailand

# Ok well I did find out the Koh Samui and Thailand part, but jfc how the hell am I supposed to guess the combination?
# I did try koh:samui at least...

# http://www.pythonchallenge.com/pc/rock/grandpa.html

# Anyway, looks like Mandlebrot.

import time
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

im = Image.open("./level31/mandelbrot.gif")
# # Welp, if it's a GIF then it's probably palette encoding
# data = list(im.getdata())
# palette = im.getpalette()
# # ok, seems like I'm correct?
# # iterations = 128. Hm...

# ok, I almost looked at the hint and then I an idea.
# What if I try to paint the mandelbrot set specified by the <window> tag at 128 iterations?

# I screwed up somewhere and I looked at the hint. Apparently I was close!
# The part that I was missing is the image size.

L = 0.34
T = 0.57
W = 0.036
H = 0.027

pix_w, pix_h = im.size

data = []
for y in range(pix_h - 1, -1, -1):
    for x in range(pix_w):
        z = complex(0, 0)
        c = complex(L + (W * x) / pix_w, T + (H * y) / pix_h)
        for i in range(128):
            z = z**2 + c
            mag = np.sqrt(np.real(z) ** 2 + np.imag(z) ** 2)
            if mag > 2:
                break
        data.append(i)

# huh? I got the exact same image...
# hint: diff the two images
# sigh...

# at this point I'm just copying the hint...

data1 = list(im.getdata())
data2 = data

diff = [(a - b) for a, b in zip(data1, data2) if a != b]
print(len(diff))

plot = Image.new("L", (23, 73))
plot.putdata([(i < 16) and 255 or 0 for i in diff])
plot.resize((230, 730)).show()

# dafuq....?
# How am I supposed to know what this is...?

# arecibo message, apparently.
# http://www.pythonchallenge.com/pc/rock/arecibo.html
