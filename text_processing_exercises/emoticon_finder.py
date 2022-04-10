def emoticon_finder(seq):
    for i in range(len(seq)):
        if seq[i] == ':':
            print(seq[i: i+2])


sequence = input()
emoticon_finder(sequence)