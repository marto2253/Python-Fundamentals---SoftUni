def reverse_string(w):
    while w != 'end':
        print(f'{w} = {w[::-1]}')
        w = input()


word = input()
reverse_string(word)
