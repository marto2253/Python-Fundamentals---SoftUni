number_of_wagons = [0 for i in range(int(input()))]

command = input()

while command != "End":
    split_command = command.split(" ")
    if split_command[0] == "add":
        number_of_wagons[-1] += int(split_command[1])
    elif split_command[0] == "insert":
        number_of_wagons[int(split_command[1])] += int(split_command[2])
    elif split_command[0] == "leave":
        number_of_wagons[int(split_command[1])] -= int(split_command[2])

    command = input()

print(number_of_wagons)