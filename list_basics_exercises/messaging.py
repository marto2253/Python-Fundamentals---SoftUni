numbers = input()
word = input()

word1 = []
split_numbers = numbers.split(" ")

final_word = ""
counter = -1

is_False = False

for y in word:
    word1.append(y)

for i in range(len(split_numbers)):
    sum_of_digits = 0
    for n in split_numbers[i]:
        sum_of_digits += int(n)
        is_False = False

    while not is_False:
        for letter in word1:
            counter += 1
            if counter == sum_of_digits:
                final_word += letter
                word1.remove(letter)
                counter = -1
                is_False = True
                break

print(final_word)



