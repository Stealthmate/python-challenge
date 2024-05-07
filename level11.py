# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image
import numpy as np

im = Image.open('./level11/cave.jpg')

pixels = np.array(im.getdata()).reshape(480, 640, 3)
odd_pixels = pixels[::2, ::2, :]

# im.show()

odd_im = Image.fromarray(np.array(odd_pixels).reshape(240, 320, 3).astype('uint8'), 'RGB')
odd_im.show()

# http://www.pythonchallenge.com/pc/return/evil.html