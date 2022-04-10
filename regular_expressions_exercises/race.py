import re


def race(seq):
    participants = {i:0 for i in names}

    while seq != 'end of race':
        name_exp = r'(?P<name>[A-Za-z]+)'
        dist_exp = r'(?P<distance>[0-9])'

        name = ''

        letter_matches = re.finditer(name_exp,seq)
        digit_matches = re.finditer(dist_exp, seq)

        for letter in letter_matches:
            name += letter.group()
        if name in participants.keys():
            for dist in digit_matches:
                participants[name] += int(dist.group())

        seq = input()

    counter = 1

    for k, v in sorted(participants.items(), key=lambda x: -x[1]):
        if counter == 1:
            print(f'1st place: {k}')
        elif counter == 2:
            print(f'2nd place: {k}')
        elif counter == 3:
            print(f'3rd place: {k}')
        counter+=1


names = input().split(', ')
sequence = input()
race(sequence)
