# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# butter fly

# ok, maybe just try to solve the maze?

from collections import deque
import typing
import zipfile

from PIL import Image, ImageDraw
import numpy as np

MARK_UNSEEN = 0
MARK_PATH = 1
MARK_WALL = 2
MARK_DEAD_END = 3
MARK_IN_PROGRESS = 4

im = Image.open('level24/maze.png').convert('RGB')
data = np.array(im.getdata()).reshape(641, 641, 3)

def neighbours_of(p: tuple[int, int]) -> typing.Iterator[tuple[int, int]]:
    if p[0] > 0:
        yield (p[0] - 1, p[1])
    if p[0] < 640:
        yield (p[0] + 1, p[1])
    if p[1] > 0:
        yield (p[0], p[1] - 1)
    if p[1] < 640:
        yield (p[0], p[1] + 1)

def is_wall(p: tuple[int, int]) -> bool:
    return np.all(data[p[0], p[1]] == 255)

solved_map = np.ones((641, 641, 1)) * MARK_UNSEEN
parents = {}
solved = False

START = (0, 639)
END = (640, 1)
import time

Q = deque()
Q.appendleft(START)
while Q:
    current = Q.pop()
    if solved_map[current] != MARK_UNSEEN:
        continue

    if is_wall(current):
        solved_map[current] = MARK_WALL
        continue

    solved_map[current] = MARK_PATH

    if current == END:
        break

    for p in neighbours_of(current):
        if solved_map[p] == MARK_UNSEEN:
            parents[p] = current
            Q.appendleft(p)

result = Image.new("RGB", (641, 641))
draw = ImageDraw.Draw(result)
for i in range(641):
    for j in range(641):
        color = ['black', 'green', 'red', 'yellow', 'blue']
        draw.point([j, i], fill=color[int(solved_map[i, j, 0])])

# depending on where you start from, half the map is unreachable.
# ok I'm stuck now.
# https://www.hackingnote.com/en/python-challenge-solutions/level-24/
# ok, this is bullshit, but apparently it's the black pixels that signify the path...

# > From the zip, a picture with the word "lake".
# how the fuck does ZIP show up here????

collected_data = []
p = END
while p != START:
    collected_data.append(int(data[p[0], p[1], 0]))
    p = parents[p]
    draw.point(p[::-1], 'blue')
# result.show()
collected_data.append(int(data[p[0], p[1], 0]))
collected_data = collected_data[::-1]
collected_data = collected_data[1::2]

print(collected_data[:10])
open('level24/maze.zip','wb').write(bytes(collected_data))

# https://www.pythonchallenge.com/pc/hex/lake.html