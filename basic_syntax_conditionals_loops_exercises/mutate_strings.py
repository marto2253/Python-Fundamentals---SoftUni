w = input()
w1 = input()

for i in range(len(w)):
    if w[i] != w1[i]:
        replacement = w[0:i] + w1[i] + w[i + 1:]
        w = replacement
        print(w)