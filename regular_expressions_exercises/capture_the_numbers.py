import re


def capture(seq):

    numbers = []
    expression = r"\d+"

    while seq:
        match = re.findall(expression, seq)
        if match:
            numbers.extend(match)
        seq = input()

    print(*numbers, sep=' ')


sequence = input()
capture(sequence)
