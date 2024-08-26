# https://www.pythonchallenge.com/pc/hex/lake.html
# ref: see mybroken.zip from previous challenge

# saw a hint from: https://www.hackingnote.com/en/python-challenge-solutions/level-25/
# "to download a wav file [...] https://www.pythonchallenge.com/pc/hex/lake1.wav"
# Dude, wtf...
# I tried interpreting the JPG files as WAV and playing them with aplay or whatever.
# But suddenly I was supposed to be scanning the URLs for WAVs????
# "imagine how they sound" my ass.

import wave

import requests
from PIL import Image
from requests.auth import HTTPBasicAuth

# i = 1
# done = False
# while not done:
#     print(i)
#     res = requests.get(f"http://www.pythonchallenge.com/pc/hex/lake{i}.wav", auth=HTTPBasicAuth('butter', 'fly'))
#     if res.status_code != 200:
#         raise Exception(res.status_code)

#     with open(f'level25/lake{i:02}.wav', mode='wb') as f:
#         f.write(res.content)

#     i += 1


# "can be converted two a 5x5 matrix of images"
# jesus

ims = []

for i in range(1, 26):
    with wave.open(f"level25/lake{i:02}.wav") as f:
        ims.append(Image.frombytes("RGB", (60, 60), f.readframes(f.getnframes())))

main_img = Image.new("RGB", (300, 300))

for i in range(5):
    for j in range(5):
        im = ims[j * 5 + i]
        main_img.paste(im, (i * 60, j * 60, (i + 1) * 60, (j + 1) * 60))

main_img.show()

# https://www.pythonchallenge.com/pc/hex/decent.html
