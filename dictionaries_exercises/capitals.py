def capitals(seq1, seq2):
    dictionary = {}
    for key, value in zip(seq1, seq2):
        dictionary[key] = value

    for k in dictionary:
        print(f'{k} -> {dictionary[k]}')


sequence = input().split(", ")
sequence2 = input().split(", ")
capitals(sequence, sequence2)