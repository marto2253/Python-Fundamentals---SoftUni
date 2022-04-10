def array_modifier():
    integers_array = list(map(int, input().split(" ")))
    commands = input()

    while commands != "end":
        command = commands.split(" ")
        action = command[0]

        if action == "swap":
            index1 = int(command[1])
            index2 = int(command[2])
            integers_array[index1], integers_array[index2] = integers_array[index2], integers_array[index1]

        elif action == "multiply":
            index1 = int(command[1])
            index2 = int(command[2])
            integers_array[index1] = integers_array[index1] * integers_array[index2]

        elif action == "decrease":
            for i in range(len(integers_array)):
                integers_array[i] -= 1

        commands = input()
    string_int_arrays = [str(i) for i in integers_array]
    print(', '.join(string_int_arrays))


array_modifier()
