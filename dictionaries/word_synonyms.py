counter = int(input())
dictionary = dict()

for i in range(counter):
    word = input()
    synonym = input()

    if word not in dictionary.keys():
        dictionary[word] = list()

    dictionary[word].append(synonym)

for k, v in dictionary.items():
    print(f'{k} - {", ".join(v)}')