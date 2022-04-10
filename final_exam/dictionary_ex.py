def dictionary(words, t_words, action):

    definitions = {}

    words = words.split(' | ')
    for word in words:
        word = word.split(': ')
        if word[0] not in definitions:
            definitions[word[0]] = [word[1]]
        else:
            definitions[word[0]].append(word[1])

    t_words = t_words.split(" | ")

    if action == 'Test':
        for word in t_words:
            for k, v in definitions.items():
                if word in k:
                    print(f'{k}:')
                    joining = "\n -".join(v)
                    print(f' -{joining}')
    elif action == 'Hand Over':
        for k in definitions.keys():
            print(k, end=' ')


all_words = input()
teacher_words = input()
actions = input()

dictionary(all_words, teacher_words, actions)