def digits_others(seq):
    letters = ''
    numbers = ''
    symbols = ''

    for i in seq:
        if i.isalnum():
            if i.isdigit():
                numbers += i
            else:
                letters += i
        else:
            symbols += i

    print(numbers)
    print(letters)
    print(symbols)


sequence = input()
digits_others(sequence)
