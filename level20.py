# http://www.pythonchallenge.com/pc/hex/idiot2.html
# "private property beyopnd this fence" but inspecting it carefully is allowed
# ok, so most likely this is a reference to the inspect module
# behind the fence there's a "field", so
# - private
# - property
# - field
# - inspect
# but what am I supposed to inspect???

# hint: https://www.hackingnote.com/en/python-challenge-solutions/level-20/
# So it is a huge file(length of 2123456789) however only a small portion is served(0 to 30202). Try to get the content after that:

# OK, I actually saw this by myself and was a bit confused, but apparently it's relevant.

import requests
import zipfile

sess = requests.Session()
sess.auth = ('butter', 'fly')

# URL = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"

# responses: list[bytes] = []

# current_pointer = 30202
# while current_pointer < 2123456789:
#     res = sess.get(URL, headers={
#         'Range': f'bytes={current_pointer + 1}-2123456789'
#     })
#     print(current_pointer)
#     current_pointer += int(res.headers.get('Content-Length', 0))
#     responses.append(res.content)
#     print(res.headers)
#     print(res.content)

# 30346
# invader?

# hint: what about content after the length?
# dafuq???? what the....
# man, you can never trust anything about this server...

URL = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
res = sess.get(URL, headers={ 'Range': 'bytes=2123456789-'})
print(res.headers)
print(res.content)

# "esrever ni emankcin wen ruoy si drowssap eht"
# "the password is your new nickname in reverse"
# so, redavni?


# hint: now reverse the search
# dafuq...
res = sess.get(URL, headers={ 'Range': 'bytes=2123456743-'})
print(res.headers)
print(res.content)

# "and it is hiding at 1152983631."

res = sess.get(URL, headers={ 'Range': 'bytes=1152983631-'})
print(res.headers)
with open('level20/hiding.zip', mode='wb') as f:
    f.write(res.content)

# ok, so apparently this is a ZIP file 
# https://www.reddit.com/r/learnprogramming/comments/bbq5lt/any_ideas_how_to_decode_this_archaic_filetype_off/

with zipfile.ZipFile('level20/hiding.zip') as f:
    f.setpassword(b'redavni')
    with f.open('readme.txt') as ff:
        print(ff.read())

# apparently this is level 21?
# oh my god...
# anyway, 20 is done I guess.
