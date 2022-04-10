import re


def destination_mapper(seq):

    destinations = []
    length = 0
    expression = r'(=|/)[A-Z][A-Za-z]{2,}\1'

    matches = re.finditer(expression, seq)

    for match in matches:
        if match:
            destinations.append(match.group()[1:-1])
            length += len(match.group()[1:-1])

    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {length}")


sequence = input()
destination_mapper(sequence)