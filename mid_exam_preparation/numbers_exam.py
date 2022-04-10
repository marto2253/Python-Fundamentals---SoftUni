sequence = list(map(int, input().split(" ")))
commands = input()
while commands != "Finish":
    command = commands.split(" ")
    if command[0] == "Add":
        sequence.append(int(command[1]))
    elif command[0] == "Remove":
        sequence.remove(int(command[1]))
    elif command[0] == "Replace":
        if int(command[1]) in sequence:
            index = sequence.index(int(command[1]))
            sequence[index] = int(command[2])
    elif command[0] == "Collapse":
        while min(sequence) < int(command[1]):
            sequence.remove(min(sequence))
    commands = input()


print(' '.join([str(i) for i in sequence]))
