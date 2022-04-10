import re


def find_var(seq):

    expression = fr"\b{word}\b"

    find = re.findall(expression, seq, re.I)

    print(len(find))


sequence = input()
word = input()
find_var(sequence)
