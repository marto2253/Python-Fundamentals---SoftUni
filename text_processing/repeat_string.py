def repeat_string(w):
    w = w.split()
    print(f'{"".join([i * len(i) for i in w])}')


words = input()
repeat_string(words)

# print(''.join([i * len(i) for i in input().split()]))