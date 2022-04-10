def replace_r_s(seq):
    new_string = ''
    for i in range(len(seq)):
        if i + 1 < len(seq):
            if seq[i + 1] != seq[i]:
                new_string += seq[i]
        else:
            new_string += seq[i]

    print(new_string)


sequence = input()
replace_r_s(sequence)
