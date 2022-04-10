product_list = input().split("!")

command = input()
while command != "Go Shopping!":
    command = command.split(" ")

    if command[0] == "Urgent":
        if command[1] not in product_list:
            product_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in product_list:
            product_list.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in product_list:
            first = product_list.index(command[1])
            product_list[first] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in product_list:
            product_list.remove(command[1])
            product_list.append(command[1])
    command = input()

print(", ".join(product_list))
