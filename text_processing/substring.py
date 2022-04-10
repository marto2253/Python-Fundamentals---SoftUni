def substring(f, s):
    while f in s:
        s = s.replace(f, '')

    print(s)


first = input()
second = input()
substring(first, second)