word = input()

list_indexes = []

for i in range(len(word)):
    if word[i].isupper():
        list_indexes.append(i)

print(list_indexes)