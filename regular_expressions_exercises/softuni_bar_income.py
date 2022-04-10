import re


def softuni_bar_income(seq):
    total = 0
    while seq != "end of shift":

        product = ''
        name = ''
        quantity = 0
        price = 0

        expression = r'%(?P<name>[A-Z][a-z]+)%(\D+)?<(?P<product>[\w]+)>(\D+)?\|(?P<quantity>[0-9]+)\|(\D+)?(?P<price>[0-9]+(\.[0-9]+)?)\$'

        matches = re.finditer(expression, seq)

        for match in matches:
            name += match.group('name')
            product += match.group('product')
            quantity += int(match.group('quantity'))
            price += float(match.group('price'))
            total += price * quantity
            print(f"{name}: {product} - {quantity * price:.2f}")

        seq = input()

    print(f"Total income: {total:.2f}")


sequence = input()
softuni_bar_income(sequence)
