def caesar_cipher(seq):
    for ch in seq:
        print(chr(ord(ch) + 3), end='')


sequence = input()
caesar_cipher(sequence)