def secret_chat(con_message, seq):

    while seq != 'Reveal':

        commands = seq.split(':|:')
        action = commands[0]

        if action == 'InsertSpace':
            index = int(commands[1])
            if index in range(len(con_message) + 1):
                con_message = con_message[:index] + ' ' + con_message[index:]

            print(con_message)

        elif action == 'Reverse':
            substring = commands[1]
            word_length = len(substring)

            if substring in con_message:
                index = con_message.find(substring)
                word = con_message[index: index + word_length]
                reversed_word = word[::-1]
                con_message = con_message[:index] + con_message[index+word_length:] + reversed_word
                print(con_message)
            else:
                print('error')

        elif action == 'ChangeAll':
            substring = commands[1]
            replacement = commands[2]

            while substring in con_message:
                con_message = con_message.replace(substring, replacement)

            print(con_message)

        seq = input()

    print(f'You have a new text message: {con_message}')

conceal_message = input()
sequence = input()
secret_chat(conceal_message,sequence)