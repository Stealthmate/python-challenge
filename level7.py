import requests
from PIL import Image

img = Image.open("level7/oxygen.png").convert("RGB")
pixels = img.load()

seq = []
gs = False
y = 48
for x in range(img.size[0]):
    if pixels[x, y][0] == pixels[x, y][1] and pixels[x, y][0] == pixels[x, y][2]:
        seq.append(pixels[x, y][0])

last_num = None
uniq_seq = []
uniq_seq = seq[::7]

uniq_seq = "".join([chr(uniq_seq[i]) for i in range(0, len(uniq_seq))])
print(len(uniq_seq))
print(uniq_seq)

arr = [105, 110, 116, 101, 103, 114, 105, 116, 121]
target = "".join(chr(c) for c in arr)
print(f"http://www.pythonchallenge.com/pc/def/{target}.html")
