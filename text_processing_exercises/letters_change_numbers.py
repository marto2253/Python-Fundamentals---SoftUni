import string


def letter_place(letter):
    if letter.isupper():
        index = string.ascii_uppercase.index(letter)
        return index + 1
    else:
        index = string.ascii_lowercase.index(letter)
        return index + 1


def l_c_n(seq):
    total = 0

    for word in seq:
        f_l = ''
        l_l = ''
        digits = ''
        for i in word:
            if i.isdigit():
                digits += i
            elif i.isalpha():
                if len(f_l) != 0:
                    l_l += i
                else:
                    f_l += i

        if f_l.isupper():
            total += float(digits) / letter_place(f_l)
        else:
            total += float(digits) * letter_place(f_l)
        if l_l.isupper():
            total -= letter_place(l_l)
        else:
            total += letter_place(l_l)

    print(f'{total:.2f}')


sequence = input().split()
l_c_n(sequence)