# http://www.pythonchallenge.com/pc/return/disproportional.html

import numpy as np
from PIL import Image

im = Image.open("level13/disprop.jpg")
im = im.crop((326 - 45 // 2, 177 - 45 // 2, 326 + 45 // 2, 177 + 45 // 2))
im.show()

# phonebook is an xmlrpc endpoint
# curl -X POST --data '@level13/example.xml' http://www.pythonchallenge.com/pc/phonebook.php

# Saw the hint for this part :(
# curl --user huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg

# http://www.pythonchallenge.com/pc/return/italy.html
