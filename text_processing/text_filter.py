def t_filter(w, t):
    for i in w:
        while i in t:
            t = t.replace(i, '*' * len(i))

    print(t)


w = input().split(', ')
t = input()
t_filter(w, t)