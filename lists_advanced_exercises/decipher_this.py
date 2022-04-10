message = input().split(" ")
message1 = message.copy()
new_list = list()
n_l = list()
for word in message:
    chars = ""
    counter = 0
    for char in word:
        if char.isdigit():
            chars += char
            counter += 1
        else:
            for i in message1:
                new_list.append(chr(int(chars)) + i[counter::])
                message1.remove(i)
                break
            break

for word in new_list:
    first_letter = ""
    last_letter = ""
    for char in range(len(word)):
        if char == 1:
            first_letter += word[char]
        if char == len(word) - 1:
            last_letter += word[char]
    if len(word) > 2:
        n_l.append(word[0] + last_letter + word[2:-1] + first_letter)
    else:
        n_l.append(word)

print(" ".join(n_l))


