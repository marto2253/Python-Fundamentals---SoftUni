def odd_occurrences(seq):
    seq_dict = dict()

    for i in seq:
        if i not in seq_dict:
            seq_dict[i] = 0

        seq_dict[i] += 1

    for k, v in seq_dict.items():
        if v % 2 != 0:
            print(k, end=" ")


sequence = input().lower().split(" ")
odd_occurrences(sequence)
