import re


def message_translator(num):
    for _ in range(num):
        seq = input()

        message = []

        pattern = r'(\!)(?P<action>[A-Z][a-z]{3,})(\1)\:\[(?P<message>[A-Za-z]{8,})\]'

        regex = re.match(pattern, seq)

        if regex:
            message.append(regex.group('message'))
            converting = []
            for word in message:
                for letter in word:
                    converting.append(str(ord(letter)))
            print(f"{regex.group('action')}: {' '.join(converting)}")
        else:
            print('The message is invalid')


number = int(input())
message_translator(number)
