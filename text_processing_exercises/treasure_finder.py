def treasure_finder(key):
    key = key.split()
    sequence = input()
    while sequence != "find":
        index = 0
        treasure_message = ''
        for i in range(len(sequence)):
            treasure_message += chr(ord(sequence[i]) - int(key[index]))
            index += 1

            if index >= len(key):
                index = 0
        t_s, t_f = treasure_message.find('&'), treasure_message.rfind('&')
        c_s, c_f = treasure_message.find('<'), treasure_message.find('>')
        print(f'Found {treasure_message[t_s +1:t_f]} at {treasure_message[c_s+1:c_f]}')

        sequence = input()


key = input()
treasure_finder(key)