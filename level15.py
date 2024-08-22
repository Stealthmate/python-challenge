# http://www.pythonchallenge.com/pc/return/uzi.html

import datetime

# used a bit of info from https://www.hackingnote.com/en/python-challenge-solutions/level-15/index.html
# "year must be 1xx6" - yeah right, that hole def has space for only 1 digit, how tf am I supposed to just "pretend" that it should be two??

for y in range(100, 2000):
    if y % 10 != 6:
        continue
    d1 = datetime.date(y, 1, 26).weekday()
    try:
        d2 = datetime.date(y, 2, 29)
    except:
        continue
    if d1 == 0:
        print(y)

# http://www.pythonchallenge.com/pc/return/mozart.html
