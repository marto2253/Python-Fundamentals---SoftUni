import sys
initial_list = list(int(i) for i in input().split(" "))
command_input = input()

list_try = list()

# min_number = sys.maxsize
# max_number = -sys.maxsize
counter = 0

while command_input != "end":
    command_input_split = command_input.split(" ")
    command = command_input_split[0]
    properties = command_input_split[1]
    min_number = sys.maxsize
    max_number = -sys.maxsize

    if command == "exchange":
        if int(properties) > len(initial_list):
            print("Invalid index")
        else:
            # l1 = initial_list[:int(properties)+1]
            # l2 = initial_list[int(properties) + 1:]
            initial_list = initial_list[int(properties) + 1:] + initial_list[:int(properties)+1]
    elif command == "max":
        if properties == "even":
            for i in initial_list:
                if i > max_number and i % 2 == 0:
                    max_number = i
            if max_number in initial_list:
                print(initial_list.index(max_number))
            else:
                print("No matches")
        elif properties == "odd":
            for i in initial_list:
                if i > max_number and i % 2 != 0:
                    max_number = i
            if max_number in initial_list:
                print(initial_list.index(max_number))
            else:
                print("No matches")
    elif command == "min":
        if properties == "even":
            for i in initial_list:
                if i < min_number and i % 2 == 0:
                    min_number = i
            if min_number in initial_list:
                print(initial_list.index(min_number))
            else:
                print("No matches")
        elif properties == "odd":
            for i in initial_list:
                if i < min_number and i % 2 != 0:
                    min_number = i
            if min_number in initial_list:
                print(initial_list.index(min_number))
            else:
                print("No matches")
    elif command == "first":
        if command_input_split[2] == "even":
            if int(properties) <= len(initial_list):
                for i in initial_list:
                    if i % 2 == 0 and counter != int(properties):
                        list_try.append(i)
                        counter += 1
                print(list_try)
                list_try.clear()
            else:
                print("Invalid count")
        elif command_input_split[2] == "odd":
            if int(properties) <= len(initial_list):
                for i in initial_list:
                    if i % 2 != 0 and counter != int(properties):
                        list_try.append(i)
                        counter += 1
                print(list_try)
                list_try.clear()
            else:
                print("Invalid count")
    elif command == "last":
        if command_input_split[2] == "even":
            if int(properties) <= len(initial_list):
                for i in range(len(initial_list)-1, -1, -1):
                    if initial_list[i] % 2 == 0 and counter != int(properties):
                        list_try.append(initial_list[i])
                        counter += 1
                print(list_try)
                list_try.clear()
            else:
                print("Invalid count")
        else:
            if int(properties) <= len(initial_list):
                for i in range(len(initial_list) - 1, -1, -1):
                    if initial_list[i] % 2 != 0 and counter != int(properties):
                        list_try.append(initial_list[i])
                        counter += 1
                print(list_try)
                list_try.clear()
            else:
                print("Invalid count")
    command_input = input()

print(initial_list)