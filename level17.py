# http://www.pythonchallenge.com/pc/return/romance.html
# used hint: apparently the image was from level 4...
# how am I supposed to remember that...

import requests
import urllib3
import urllib.parse
import bz2

sess = requests.Session()
# nothing = '12345'
# seen = set()
# buffer = []
# while nothing:
#     if nothing in seen:
#         break
#     res = sess.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={nothing}')
#     header = res.headers.get('Set-Cookie')
#     # print(header)
#     letter = header[5:header.index(';')]
#     if letter == 'deleted':
#         break
#     # print(letter)
#     buffer.append(letter)
#     seen.add(nothing)
#     nothing = res.text.split(' ')[-1]
#     # print(nothing)
# buffer = urllib.parse.unquote_to_bytes(''.join(buffer))
# print(bz2.decompress(buffer))
# b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'


# curl -X POST --data '@level17.xml' http://www.pythonchallenge.com/pc/phonebook.php
# 555-VIOLIN
# http://www.pythonchallenge.com/pc/return/violin.html
# http://www.pythonchallenge.com/pc/stuff/violin.php

sess.cookies.set("info", "the flowers are on their way")
res = sess.get(f'http://www.pythonchallenge.com/pc/stuff/violin.php')
print(res.text)

# http://www.pythonchallenge.com/pc/return/balloons.html