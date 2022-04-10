sequence = input().split(", ")
commands = input()

while commands != "End":
    command = commands.split(" - ")
    if command[0] == "Add":
        if command[1] not in sequence:
            sequence.append(command[1])
    elif command[0] == "Remove":
        if command[1] in sequence:
            sequence.remove(command[1])
    elif command[0] == "Bonus phone":
        phones = command[1].split(":")
        if phones[0] in sequence:
            index = sequence.index(phones[0])
            sequence.insert(index + 1, phones[1])
    elif command[0] == "Last":
        if command[1] in sequence:
            sequence.remove(command[1])
            sequence.insert(len(sequence), command[1])
    commands = input()

print(', '.join(sequence))
