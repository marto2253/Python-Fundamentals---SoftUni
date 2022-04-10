def imitation_game(seq, initial_message):
    while seq != 'Decode':
        operation = seq.split("|")

        if operation[0] == 'Move':
            # temp = list()
            num = int(operation[1])
            initial_message = initial_message[num:] + initial_message[:num]
            # for i in range(len(initial_message), -1, -1):
            #     if i < num:
            #         l = initial_message.pop(i)
            #         temp.append(l)
            # initial_message.extend(reversed(temp))
        elif operation[0] == 'ChangeAll':
            current = operation[1]
            replacement = operation[2]
            while current in initial_message:
                index = initial_message.index(current)
                initial_message[index] = replacement
        elif operation[0] == 'Insert':
            num = int(operation[1])
            letter = operation[2]

            initial_message.insert(num, letter)

        seq = input()

    print(f'The decrypted message is: {"".join(initial_message)}')


initial_message = list(input())
sequence = input()
imitation_game(sequence, initial_message)

