def hogwarts(seq):
    commands = input()

    while commands != 'Abracadabra':
        valid_commands = ['Abjuration', 'Necromancy', 'Illusion', 'Divination', 'Alteration']
        commands = commands.split()

        action = commands[0]

        if action not in valid_commands:
            print("The spell did not work!")
        elif action == 'Abjuration' and action in valid_commands:
            seq = seq.upper()
            print(seq)
        elif action == 'Necromancy' and action in valid_commands:
            seq = seq.lower()
            print(seq)
        elif action == 'Illusion' and action in valid_commands:
            index = int(commands[1])
            replacement = commands[2]
            if 0 <= index < len(seq):
                seq = seq[:index] + replacement + seq[index+1:]
                print('Done!')
            else:
                print("The spell was too weak.")

        elif action == 'Divination' and action in valid_commands:
            first_str = commands[1]
            second_str = commands[2]

            if first_str in seq:
                while first_str in seq:
                    seq = seq.replace(first_str, second_str)
            print(seq)

        elif action == 'Alteration' and action in valid_commands:
            substring = commands[1]

            if substring in seq:
                seq = seq.replace(substring, '')
            print(seq)

        commands = input()


sequence = input()
hogwarts(sequence)
