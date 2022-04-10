def world_tour(seq):

    commands = input()

    while commands != "Travel":
        command = commands.split(':')

        if command[0] == 'Add Stop':
            index = int(command[1])
            word = command[2]
            if index in range(len(seq) + 1):
                seq = seq[:index] + word + seq[index:]

        elif command[0] == 'Remove Stop':
            start_index = int(command[1])
            end_index = int(command[2])

            if start_index in range(len(seq) + 1) and end_index in range(len(seq) + 1):

                seq = seq[:start_index] + seq[end_index + 1:]

        elif command[0] == 'Switch':
            old_word = command[1]
            new_word = command[2]

            # while seq.find(word) != -1:
            #     occurrence = seq.find(word)
            #     length = len(word)
            #     seq = seq[:occurrence] + new_word + seq[occurrence+length:]
            if old_word in seq:
                seq = seq.replace(old_word, new_word)

        print(seq)

        commands = input()

    print(f'Ready for world tour! Planned stops: {seq}')


sequence = input()
world_tour(sequence)
