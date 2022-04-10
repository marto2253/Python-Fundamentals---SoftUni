meerkat = []

for _ in range (3):
    word = input()
    meerkat.append(word)

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)