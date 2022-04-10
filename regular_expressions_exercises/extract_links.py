import re

expression = r"www.([A-Za-z0-9-]+)\.([\.a-z]+)"

seq = input()
while seq:

    matches = re.finditer(expression, seq)
    if matches:
        print(''.join([i.group() for i in matches]))

    seq = input()