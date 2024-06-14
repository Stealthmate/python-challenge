# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image
import numpy as np
import time

im = Image.open('level14/wire.png')
# im.show()

data = np.array(im.getdata()).reshape(10000, 3)

unspiral = np.zeros((100, 100, 3))
current_length = 100
current_count = 1
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
current_move = 0
current_pos = (0, -1)

i = 0

while current_length > 0:
    for j in range(i, i + current_length):
        print(current_pos)
        current_pos = tuple(current_pos[i] + move[current_move][i] for i in range(2))
        unspiral[current_pos] = data[j]
    i += current_length
    current_move = (current_move + 1) % 4
    current_count += 1
    if current_count == 2:
        current_length -= 1
        current_count = 0

im2 = Image.fromarray(np.array(unspiral).reshape(100, 100, 3).astype('uint8'), 'RGB')
im2.show()

# http://www.pythonchallenge.com/pc/return/cat.html -> uzi
# http://www.pythonchallenge.com/pc/return/uzi.html
