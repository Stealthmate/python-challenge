# import zipfile
# 
# with zipfile.ZipFile('level20/hiding.zip') as f:
    # f.setpassword(b'redavni')
    # for file in f.filelist:
        # print(file)
    # with f.open('readme.txt') as ff:
        # print(ff.read().decode())

import zlib
import bz2

buffer: bytes = b''
with open('level21/package.pack', mode='rb') as f:
    buffer = f.read()

def loop_zlib(buf: bytes) -> bytes:
    i = 0
    while buf.startswith(b'\x78\x9c'):
        print(' ', end='')
        i += 1
        buf = zlib.decompress(buf)
    return buf

def loop_bzip(buf: bytes) -> bytes:
    i = 0
    while buf.startswith(b'BZh9'):
        print('*', end='')
        i += 1
        # print(i)
        buf = bz2.decompress(buf)
    return buf

while buffer.startswith(b'\x78\x9c'):
    buffer = loop_zlib(buffer)
    buffer = loop_bzip(buffer)
    # look backwards = invert the bytes
    if buffer.endswith(b'\x9c\x78'):
        print('')
        buffer = buffer[::-1]

print(buffer[::-1])
# look at your logs
# hint: https://www.hackingnote.com/en/python-challenge-solutions/level-21/
# hell no, this is way too much of a conceptual jump..., sigh

# copper
# http://www.pythonchallenge.com/pc/hex/copper.html