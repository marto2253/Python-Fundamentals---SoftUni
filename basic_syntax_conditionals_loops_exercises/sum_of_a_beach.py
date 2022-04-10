string = input()

words = ['sand', 'water', 'fish', 'sun']

words_counter = 0
for i in words:
    x = string.lower().count(i)
    if x:
        words_counter += x

print(words_counter)