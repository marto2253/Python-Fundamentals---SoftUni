def char_multiplier(seq):
    w1 = seq[0]
    w2 = seq[1]
    total = 0

    if len(w1) > len(w2):
        for i in range(len(w1)):
            if i >= len(w2):
                total += ord(w1[i])
            else:
                total += ord(w2[i]) * ord(w1[i])
    else:
        for i in range(len(w2)):
            if i >= len(w1):
                total += ord(w2[i])
            else:
                total += ord(w2[i]) * ord(w1[i])
    print(total)


sequence = input().split()
char_multiplier(sequence)