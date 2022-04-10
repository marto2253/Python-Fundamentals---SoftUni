def memory_game(sequence):
    commands = input()
    moves = 0
    while commands != "end":
        moves += 1
        command = commands.split(" ")
        index1 = int(command[0])
        index2 = int(command[1])
        if command[0] == commands[1] or int(command[0]) >= len(sequence) or int(command[1]) >= len(sequence) \
                or int(command[0]) < 0 or int(command[1]) < 0:
            sequence.insert(len(sequence) // 2, f'{-moves}a')
            sequence.insert(len(sequence) // 2, f'{-moves}a')
            print("Invalid input! Adding additional elements to the board")
        elif sequence[index1] == sequence[index2]:
            print(f"Congrats! You have found matching elements - {sequence[index1]}!")
            left_item = sequence[index1]
            sequence.remove(left_item)
            sequence.remove(left_item)
        elif sequence[index1] != sequence[index2]:
            print(f"Try again!")

        if len(sequence) == 0:
            print(f"You have won in {moves} turns!")
            break

        commands = input()

    if len(sequence) > 0:
        print(f"Sorry you lose :(\n{' '.join(sequence)}")


sequence_elements = [i for i in input().split(" ")]
memory_game(sequence_elements)
