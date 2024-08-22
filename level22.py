# http://www.pythonchallenge.com/pc/hex/copper.html
# hint: https://www.hackingnote.com/en/python-challenge-solutions/level-22/
# emulate a pen stroke
# shift letter on dx==dy==0
# lol, i am definitely not smart enough to come up with this shit

import numpy as np
from PIL import Image, ImageDraw

ims = []
result = Image.new("RGB", (500, 500))
cx, cy = 200, 200
draw = ImageDraw.Draw(result)

with Image.open("level22/white.gif") as im:
    for i in range(im.n_frames):
        im.seek(i)
        im2 = im.convert("RGB")
        data = np.array(im2.getdata())
        d = np.where(data > 0)[0][0]
        y, x = d // 200, d % 200
        dx = (x - 100) // 2
        dy = (y - 100) // 2
        if dx == dy == 0:
            cx += 50
            cy = 200
        cx += dx
        cy += dy
        draw.point([cx, cy])

result.show()

# http://www.pythonchallenge.com/pc/hex/bonus.html
