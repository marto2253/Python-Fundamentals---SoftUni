import re


def star_enigma(num):
    attacked = []
    destroyed = []
    for i in range(num):
        count = 0
        seq = input()
        message = ''
        letters = ['s', 't', 'a', 'r']
        for letter in letters:
            count += seq.lower().count(letter)

        for lett in seq:
            message += chr(ord(lett) - count)

        expression = r'@(?P<name>[A-Za-z]+)(\w)?:(?P<population>[0-9]+)(\w)?!(?P<attack_type>[AD])!(\w)?->(?P<soldiers>[0-9]+)'
        matches = re.finditer(expression, message)

        for match in matches:
            if match.group('attack_type') == 'D':
                destroyed.append(match.group('name'))
            else:
                attacked.append(match.group('name'))

    print(f'Attacked planets: {len(attacked)}')
    for item in sorted(attacked):
        print(f'-> {item}')
    # print('-> '.join(i for i in attacked))
    print(f'Destroyed planets: {len(destroyed)}')
    for item in sorted(destroyed):
        print(f'-> {item}')


number = int(input())
star_enigma(number)
