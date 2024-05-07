# http://www.pythonchallenge.com/pc/return/evil.html

# dafuq, I wouldn't have noticed without looking at the hint: https://bigeast.github.io/pythonchallenge.html

from PIL import Image

with open('level12/evil2.gfx', mode='rb') as original:
    files = [
        open(fp, mode='wb')
        for fp in [
            "level12/img0.jfif",
            "level12/img1.png",
            "level12/img2.gif",
            "level12/img3.png",
            "level12/img4.jfif",
        ]
    ]
    for i in range(13515):
        for file in files:
            file.write(original.read(1))
    for file in files:
        file.close()

# http://www.pythonchallenge.com/pc/return/disproportional.html