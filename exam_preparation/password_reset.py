init_pass = input()
seq = input()

current_pass = init_pass

while seq != 'Done':

    seq = seq.split()

    if seq[0] == 'TakeOdd':
        new_pass = current_pass
        current_pass = ''.join([new_pass[i] for i in range(len(new_pass)) if i % 2 != 0])
        print(current_pass)

    elif seq[0] == 'Cut':
        index = int(seq[1])
        length = int(seq[2])

        if index + length in range(len(current_pass) + 1):

            current_pass = current_pass[:index] + current_pass[index+length:]
            print(current_pass)

    elif seq[0] == 'Substitute':
        substring = seq[1]
        substitude = seq[2]

        if substring in current_pass:
            current_pass = current_pass.replace(substring, substitude)
            print(current_pass)
        else:
            print("Nothing to replace!")

    seq = input()

print(f'Your password is: {current_pass}')




