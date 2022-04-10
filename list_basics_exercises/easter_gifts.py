gifts = input().split(" ")
command = input().split(" ")

while command[0] != "No" and command[1] != "Money":
    if command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = "None"
    if command[0] == "Required":
        number = int(command[2])
        if len(gifts) > number > 0:
            gifts[number] = command[1]
    if command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split(" ")

for i in gifts:
    if i != "None":
        print(i, end=" ")