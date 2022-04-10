vowels = 'a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I'

no_vowels = list('' if i in vowels else i for i in input())

print("".join(no_vowels))
