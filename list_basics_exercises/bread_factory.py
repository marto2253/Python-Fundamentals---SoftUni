sequence = input().split("|")
chunked_sequence = list()

energy = 100
coins = 100

for item in sequence:
    item_info = item.split("-")
    command = item_info[0]
    number = int(item_info[1])
    if command == "rest":
        if energy + number <= 100:
            energy += number
            print(f"You gained {number} energy.")
        else:
            print(f"You gained {number - number} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            print(f"You had to rest!")
            if energy + 50 > 100:
                energy = 100
            else:
                energy += 50
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
