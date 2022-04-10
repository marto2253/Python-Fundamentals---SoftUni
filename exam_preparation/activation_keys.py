def activation_key(seq):

    commands = input()

    while commands != 'Generate':

        commands = commands.split('>>>')

        command = commands[0]

        if command == 'Contains':
            substring = commands[1]

            if substring in seq:
                print(f'{seq} contains {substring}')
            else:
                print(f'Substring not found!')

        elif command == 'Flip':
            case = commands[1]
            start_index = int(commands[2])
            end_index = int(commands[3])

            if start_index in range(len(seq) + 1) and end_index in range(len(seq) + 1):
                if case == 'Upper':
                    seq = seq[:start_index] + seq[start_index:end_index].upper() + seq[end_index:]
                    print(seq)
                elif case == 'Lower':
                    seq = seq[:start_index] + seq[start_index:end_index].lower() + seq[end_index:]
                    print(seq)

        elif command == 'Slice':
            start_index = int(commands[1])
            end_index = int(commands[2])

            if start_index in range(len(seq) + 1) and end_index in range(len(seq) + 1):
                seq = seq[:start_index] + seq[end_index:]
                print(seq)

        commands = input()

    print(f"Your activation key is: {seq}")


sequence = input()
activation_key(sequence)
