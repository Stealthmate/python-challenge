# http://www.pythonchallenge.com/pc/hex/bin.html
# cat level19/level19.b64| tr -d '\n' | base64 -d | aplay
# "sorry"

import wave

# indian -> endian
# aplay says file is S16_LE, so let's try swapping the bytes to make it S16_BE
with wave.open('level19/sorry-1.wav', mode='wb') as fo:
    with wave.open('level19/sorry.wav', mode='rb') as fi:
        print(fi.getparams())
        data = fi.readframes(int(1e9))
        t1 = data[::2]
        t2 = data[1::2]
        data = list(data)
        data[::2] = t2
        data[1::2] = t1
        final_data = b''.join([bytes([x]) for x in data])
        print(final_data)
        fo.setparams(fi.getparams())
        fo.writeframes(final_data)

# "you are an idiot" lol
# http://www.pythonchallenge.com/pc/hex/idiot.html
# http://www.pythonchallenge.com/pc/hex/idiot2.html