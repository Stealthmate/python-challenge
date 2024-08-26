# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

# relax you are on 30
# This picture is only meant to help you relax
# while you look at the csv file.

# OK then, as expected we got a CSV at
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv
# aaaaand it's a bunch of floats!?!?!?!?!?!?

# Guess I should try plotting them?

from PIL import Image, ImageOps

data = []
with open("./level30/yankeedoodle.csv") as f:
    data = [x.strip() for x in f.read().split(",") if x.strip() != ""]

# data[-1].append(1.0)

# data = np.array(data)
# plt.plot(data[5])
# plt.show()

# nope, nothing. Just noise?

# hint: factors
# Ok, so this is how you find the width/height and then produce an image.
# Sigh...

print(len(data))
print(list(x for x in range(2, len(data)) if len(data) % x == 0))
# 53, 139

float_data = [float(x) for x in data]

im = Image.new("F", (53, 139))
im.putdata(float_data, 256)
im = ImageOps.mirror(im)
im = im.rotate(90, expand=True)
im.show()

# n = str(x[i])[5]
#   + str(x[i+1])[5]
#   + str(x[i+2])[6]

decoded = []
for i in range(0, len(data) - 2, 3):
    print(data[i], data[i + 1], data[i + 2])
    x = data[i][5] + data[i + 1][5] + data[i + 2][6]
    decoded.append(int(x))
    if decoded[-1] > 255:
        raise Exception()

print(bytes(decoded))

# Had to look at the hint since I couldn't decode at first.
# Turns out hint was wrong as well - we don't have to flip and rotate the data,
# but we need to combine every 3 chars separately, instead of incrementing by 1 at each step.

# look at grandpa
# http://www.pythonchallenge.com/pc/ring/grandpa.html
