import re


def find_var(seq):

    expression = r"\b_[A-Za-z0-9]+\b"

    find = re.findall(expression, seq)

    join_to_str = ','.join(find)
    print(join_to_str.replace('_',''))

sequence = input()
find_var(sequence)
