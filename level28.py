# http://www.pythonchallenge.com/pc/ring/bell.html
# repeat
# switch

# ring-ring-ring-ring-ring...
# green?

# http://www.pythonchallenge.com/pc/ring/green.html
# Yes, green!

# many pairs ring-ring
# many pairs...

# hint: # calculate diff for every two bytes
# Jesus, again with this??

import numpy as np
from PIL import Image

im = Image.open("level28/bell.png")
data = np.array(im.getchannel("G").getdata())

diff = list(np.abs(data[:-1:2] - data[1::2]).astype("uint8"))

# hint: # remove the most frequent value 42
# wat.

diff = [x for x in diff if x != 42]

print(bytes(diff))
# whodunnit().split()[0] ?

# > The creator of Python is Guido van Rossum, so the final answer is "guido"
# Man, I give up.

# http://www.pythonchallenge.com/pc/ring/guido.html
