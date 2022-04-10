import re

sequence = input()

find = re.finditer(r"\+359([ -])2\1[0-9]{3}\1[0-9]{4}\b", sequence)

print(', '.join([str(i.group()) for i in find]))
