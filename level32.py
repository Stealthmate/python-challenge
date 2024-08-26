# http://www.pythonchallenge.com/pc/rock/arecibo.html
# Ok, this seems easy actually.

import typing

# N = 9

# rows = [
#     [2, 1, 2],
#     [1, 3, 1],
#     [5],
#     [7],
#     [9],
#     [3],
#     [2, 3, 2],
#     [2, 3, 2],
#     [2, 3, 2]
# ]

# columns = [
#     [2, 1, 3],
#     [1, 2, 3],
#     [3],
#     [8],
#     [9],
#     [8],
#     [3],
#     [1, 2, 3],
#     [2, 1, 3]
# ]

N = 32
rows = [
    [3, 2],
    [8],
    [10],
    [3, 1, 1],
    [5, 2, 1],
    [5, 2, 1],
    [4, 1, 1],
    [15],
    [19],
    [6, 14],
    [6, 1, 12],
    [6, 1, 10],
    [7, 2, 1, 8],
    [6, 1, 1, 2, 1, 1, 1, 1],
    [5, 1, 4, 1],
    [5, 4, 1, 4, 1, 1, 1],
    [5, 1, 1, 8],
    [5, 2, 1, 8],
    [6, 1, 2, 1, 3],
    [6, 3, 2, 1],
    [6, 1, 5],
    [1, 6, 3],
    [2, 7, 2],
    [3, 3, 10, 4],
    [9, 12, 1],
    [22, 1],
    [21, 4],
    [1, 17, 1],
    [2, 8, 5, 1],
    [2, 2, 4],
    [5, 2, 1, 1],
    [5],
]
columns = [
    [5],
    [5],
    [5],
    [3, 1],
    [3, 1],
    [5],
    [5],
    [6],
    [5, 6],
    [9, 5],
    [11, 5, 1],
    [13, 6, 1],
    [14, 6, 1],
    [7, 12, 1],
    [6, 1, 11, 1],
    [3, 1, 1, 1, 9, 1],
    [3, 4, 10],
    [8, 1, 1, 2, 8, 1],
    [10, 1, 1, 1, 7, 1],
    [10, 4, 1, 1, 7, 1],
    [3, 2, 5, 2, 1, 2, 6, 2],
    [3, 2, 4, 2, 1, 1, 4, 1],
    [2, 6, 3, 1, 1, 1, 1, 1],
    [12, 3, 1, 2, 1, 1, 1],
    [3, 2, 7, 3, 1, 2, 1, 2],
    [2, 6, 3, 1, 1, 1, 1],
    [12, 3, 1, 5],
    [6, 3, 1],
    [6, 4, 1],
    [5, 4],
    [4, 1, 1],
    [5],
]


def generate_tuples_to_sum(
    s: int, n: int, start: int = 0
) -> typing.Iterator[list[int]]:
    if n == 1:
        yield [s]
        return
    if s == 0:
        if n <= 2:
            yield [0] * n
            return
    for i in range(start, s + 1):
        for x in generate_tuples_to_sum(s - i, n - 1, 1):
            yield [i, *x]


def generate_row_patterns(seq: list[int]) -> typing.Iterator[list[bool]]:
    slack_slots = len(seq) + 1
    slack = N - sum(seq)
    for pattern in generate_tuples_to_sum(slack, slack_slots):
        result = [False] * pattern[0]
        for i, x in enumerate(pattern[1:]):
            result.extend([True] * seq[i])
            result.extend([False] * x)
        yield result


def scan_column(c: list[bool]) -> tuple[int, int]:
    last_length = 0
    seqs = []
    for x in c:
        if last_length > 0 and not x:
            seqs.append(last_length)
        last_length = last_length + 1 if x else 0
    if last_length > 0:
        seqs.append(last_length)
    return len(seqs), last_length


class Nope(Exception):
    pass


def test_pattern(top: list[list[bool]]) -> bool:
    print()
    print("testing pattern")
    for x in top:
        print("".join([("O" if y else "_") for y in x]))

    for i in range(N):
        try:
            column = columns[i]
            seq_id, seq_len = scan_column([x[i] for x in top])

            if seq_id > len(column):
                raise Nope(["Contains more seqs than necessary.", seq_id, len(column)])

            if seq_id > 0 and len(column) > 0:
                col_seq = column[seq_id - 1]
                if seq_len > col_seq:
                    raise Nope(
                        [
                            "Contains more true in seq than necessary",
                            seq_id,
                            seq_len,
                            col_seq,
                        ]
                    )

            remaining_fill = N - len(top)
            # print('remainig fill', remaining_fill)
            required_fill = (
                sum(column) - sum([column[j] for j in range(seq_id)]) - seq_len
            )
            # print('required fill', required_fill)

            if required_fill > remaining_fill:
                raise Nope(("Cannot be filled.", remaining_fill, required_fill))
        except Nope as ex:
            print("failed because of column", i, ex)
            return False
    print("Passed!")
    return True


def solve(top: list[list[bool]]):
    print("Trying", len(top))
    if len(top) == N:
        return top
    next_row = rows[len(top)]
    # print('next', next_row)
    for pattern in generate_row_patterns(next_row):
        # print('pattern')
        next_top = [*top, pattern]
        tested = test_pattern(next_top)
        # print('tested', tested)
        if not tested:
            continue
        # print('Diving', len(top))
        solution = solve(next_top)
        if solution is not None:
            return solution
    return


solution = solve([])
print()
print()
print("Final solution")
if solution is not None:
    for x in solution:
        for y in x:
            print("O" if y else "_", end="")
        print()

# arrow upwards. up.txt? (saw hint)

# ok I got this far but this is a shitty slow solution. Apparently there's a faster one,
# but it's been 3h already and I don't really like algorithmic puzzles to begin with, so I'm skipping.

# Apparently the answer is python.html
# free as in free ber
# http://www.pythonchallenge.com/pc/rock/beer.html
