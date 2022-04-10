def explosion(seq):
    new_string = ''
    power = 0
    for i in range(len(seq)):
        if power != 0:
            if seq[i] != ">":
                new_string += ''
                power -= 1
            else:
                new_string += seq[i]
                power += int(seq[i+1])
        elif seq[i] == '>':
            new_string += seq[i]
            power += int(seq[i+1])
        else:
            new_string += seq[i]

    print(new_string)


sequence = input()
explosion(sequence)
