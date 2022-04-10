sequence_targets = list(map(int, input().split(" ")))

commands = input()

while commands != "End":
    commands_split = commands.split(" ")
    command = commands_split[0]
    index = int(commands_split[1])
    effect = int(commands_split[2])

    if command == "Shoot":
        if index in range(len(sequence_targets)):
            if sequence_targets[index] - effect <= 0:
                sequence_targets.pop(index)
            else:
                sequence_targets[index] -= effect
    elif command == "Add":
        if index in range(len(sequence_targets)):
            sequence_targets.insert(index, effect)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if index - effect in range(len(sequence_targets)) and index + effect in range(len(sequence_targets)):
            sequence_targets = sequence_targets[0: index - effect] + sequence_targets[index + effect + 1::]
        else:
            print("Strike missed!")

    commands = input()

print('|'.join(str(i) for i in sequence_targets))
