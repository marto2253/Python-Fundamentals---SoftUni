import re

sequence = input()

find = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", sequence)

print(' '.join(find))