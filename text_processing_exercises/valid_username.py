def valid_username(seq):
    for word in seq:
        if 3 <= len(word) <= 16:
            if word.isalnum():
                print(word)
            else:
                if '-' in word or '_' in word:
                    print(word)


sequence = input().split(', ')
valid_username(sequence)
