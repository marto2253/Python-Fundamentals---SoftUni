def count_chars(seq):
    strings = dict()
    for i in seq:
        if i not in strings:
            strings[i] = 0

        strings[i] += 1

    for k, v in strings.items():
        print(f'{k} -> {v}')


sequence = input().replace(' ', '')
count_chars(sequence)
