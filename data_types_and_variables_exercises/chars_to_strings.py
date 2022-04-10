def concat():
    one_string = ""
    for i in range(3):
        character = input()
        one_string += character
    return one_string

print(concat())
