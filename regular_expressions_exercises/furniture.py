import re


def furniture(seq):

    total = []
    expression = r'>>(?P<name>[\D]+)<<(?P<price>[\d]+\.?[\d]+?)!(?P<quantity>\d)'
    name = []
    while seq != "Purchase":
        matches = re.finditer(expression, seq)
        for match in matches:
            name.append(match.group('name'))
            total.append(float(match.group('price')) * int(match.group('quantity')))

        seq = input()

    print("Bought furniture:")
    print('\n'.join(name))
    print(f'Total money spend: {sum(total):.2f}')


sequence = input()
furniture(sequence)
