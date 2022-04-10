import re

def extract_emails(seq):

    expression = r"\b(^|(?<=\s))([A-Za-z0-9]+)(\.|_|-)?([A-Za-z0-9]+)?@([A-Za-z0-9]+)(-)?([A-Za-z0-9])+?(\.)([A-Za-z0-9]+)(\.)?([A-Za-z0-9]+)?\b"

    find = re.finditer(expression, seq)

    for i in find:
        print(f'{i.group()}')


sequence = input()
extract_emails(sequence)