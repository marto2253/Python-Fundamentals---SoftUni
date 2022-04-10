sequence = input().split(" ")
food_dict = dict()

for i in range(0, len(sequence), 2):
    food = sequence[i]
    quantity = sequence[i+1]
    food_dict[food] = int(quantity)

print(food_dict)

