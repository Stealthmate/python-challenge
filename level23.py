# http://www.pythonchallenge.com/pc/hex/bonus.html
# butter fly

# picture of a cow -> cowsay?
# owe someone an apology -> Mozart?
# va gur... -> googling this led me to
# https://qiita.com/pyjackal/items/cfdb55051b1d3307eca1
# which lead me to the 'this' module in python
# Apparently the string is rot13 encoded.

import codecs
print(codecs.decode('va gur snpr bs jung', 'rot_13'))

# in the face of what? -> ambiguity (see https://qiita.com/pyjackal/items/cfdb55051b1d3307eca1 again)
# yay!

# http://www.pythonchallenge.com/pc/hex/ambiguity.html