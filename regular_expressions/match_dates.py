import re

sequence = input()

expression = r"\b(?P<day>[0-9]{2})([./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>[0-9]{4})\b"

# find = re.finditer(expression, sequence)  # if you would like to print it by the group name
find = re.findall(expression, sequence)  # if you would like to print it with indexes of the group

for i in find:
    print(f'Day: {i[0]}, Month: {i[2]}, Year: {i[3]}')
    # print(f'Day: {i.group("day")}, Month: {i.group("month")}, Year: {i.group("year")}')




