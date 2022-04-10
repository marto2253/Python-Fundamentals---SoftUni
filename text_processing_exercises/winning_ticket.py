def winning_ticket(seq):
    for i in seq:
        sign = 0
        dies = 0
        at = 0
        arrow = 0
        special_char = ''
        if len(i) == 20:
            first_part = i[:10]
            second_part = i[10:]
            for char in first_part:
                if not char.isalnum():
                    if first_part.count(special_char) == 10:
                        break
                    if char == '$':
                        special_char = '$'
                        sign += 1
                    elif char == '#':
                        special_char = '#'
                        dies += 1
                    elif char == '@':
                        special_char = '@'
                        at += 1
                    elif char == '^':
                        special_char = '^'
                        arrow += 1

            for char in second_part:
                if not char.isalnum():
                    if first_part.count(special_char) == 10 and second_part.count(special_char) == 10:
                        print(f'ticket "{i}" - {20 // 2}{special_char} Jackpot!')
                        break
                    if char == '$':
                        sign += 1
                    elif char == '#':
                        dies += 1
                    elif char == '@':
                        at += 1
                    elif char == '^':
                        arrow += 1

            if sign == 12 or dies == 12 or at == 12 or arrow == 12:
                print(f'ticket "{i}" - {(12//2)}{special_char}')
            else:
                print(f'ticket "{i}" - no match')
        else:
            print('invalid ticket')


sequence = input().replace(' ', '').split(',')
winning_ticket(sequence)
