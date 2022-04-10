def ascii_sumator(f_c, s_c, seq):
    total = 0
    for i in seq:
        if ord(f_c) < ord(i) < ord(s_c):
            total += ord(i)

    print(total)


first_char = input()
second_char = input()
sequence = input()
ascii_sumator(first_char, second_char, sequence)