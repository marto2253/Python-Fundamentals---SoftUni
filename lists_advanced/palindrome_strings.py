sequence = [i for i in input().split(" ")]
word = input()

palindrome = list()

palin = [i for i in sequence if i == i[::-1]]

# for i in sequence:
#     reversed_word = i[::-1]
#     if i == reversed_word:
#         palindrome.append(i)

print(palin)
print(f"Found palindrome {sequence.count(word)} times")
