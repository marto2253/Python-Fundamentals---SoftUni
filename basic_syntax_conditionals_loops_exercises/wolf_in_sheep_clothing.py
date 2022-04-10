text = input()
text_list = text.split(", ")
counter = -1

for i in range(len(text_list) -1, -1, -1):
    counter += 1
    if text_list[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if text_list[i] == "wolf" and text_list[-1] != "wolf":
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")

