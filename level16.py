# http://www.pythonchallenge.com/pc/return/uzi.html
# used a bit of info from https://www.hackingnote.com/en/python-challenge-solutions/level-16/index.html
# Sounds like we need to align the pink segments. But how do you define "pink"

from PIL import Image
import numpy as np

im = Image.open('level16/mozart.gif').convert('RGB')
data = np.array(im.getdata()).reshape(480, 640, 3)

for i in range(data.shape[0]):
    row = data[i, :]
    initial_pink = 0
    for j in range(row.shape[0] - 6):
        next_5 = [
            tuple(row[k, :])
            for k in range(j, j + 6)
        ]
        if (
            next_5[0] == next_5[1]
            and next_5[0] == next_5[2]
            and next_5[0] == next_5[3]
            and next_5[0] == next_5[4]
            and next_5[0][0] > 200
            and next_5[0][1] < 200
        ):
            initial_pink = j
            break
    if initial_pink == 0:
        for pix in row:
            print(pix)
        raise Exception()
    data[i] = np.concatenate([row[initial_pink:], row[:initial_pink]], axis=0)

final_im = Image.fromarray(np.array(data).astype('uint8'), 'RGB')
final_im.save("level16/aligned.png", "PNG")

# http://www.pythonchallenge.com/pc/return/romance.html