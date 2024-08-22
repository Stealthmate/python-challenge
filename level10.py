# http://www.pythonchallenge.com/pc/return/bull.html


# http://www.pythonchallenge.com/pc/return/sequence.txt
# a = [1, 11, 21, 1211, 111221, ... ]

## Hmm..
## one, one one, two ones, one two and one one, one one, one two, two ones
## Seen this on numberphile before lol.
## https://www.youtube.com/watch?v=ea7lJkEhytA
a = [1]

while len(a) < 31:
    last = str(a[-1])
    current_digit = last[0]
    current_count = 1
    next_number = ""
    for d in last[1:]:
        if d == current_digit:
            current_count += 1
        else:
            next_number = f"{next_number}{current_count}{current_digit}"
            # print(current_count, current_digit)
            current_digit = d
            current_count = 1
    next_number = f"{next_number}{current_count}{current_digit}"
    a.append(next_number)

print(a[30], len(a[30]))

# http://www.pythonchallenge.com/pc/return/5808.html
