coffee = 0
while True:
    text = input()
    if text == "END":
        if coffee > 5:
            print("You need extra sleep")
        else:
            print(coffee)
        break
    if text == "coding" or text == "dog" or text == "cat" or text == "movie":
        coffee += 1
    if text == "CODING" or text == "DOG" or text == "CAT" or text == "MOVIE":
        coffee += 2

