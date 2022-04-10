def character_range_ascii(char1, char2):
    start = ord(char1) + 1
    finish = ord(char2)

    for i in range(start, finish):
        print(chr(i), end=" ")


character_one = input()
character_two = input()

character_range_ascii(character_one, character_two)
