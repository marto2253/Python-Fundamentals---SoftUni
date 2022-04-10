line_one = input().split(" ")
line_two = input().split(" ")
line_three = input().split(" ")

one_list = list(line_one + line_two + line_three)

if one_list[0] == one_list[1] == one_list[2] == "1" or \
    one_list[3] == one_list[4] == one_list[5] == "1" or \
    one_list[6] == one_list[7] == one_list[8] == "1" or \
    one_list[0] == one_list[3] == one_list[6] == "1" or \
    one_list[1] == one_list[4] == one_list[7] == "1" or \
    one_list[2] == one_list[5] == one_list[8] == "1" or \
    one_list[0] == one_list[4] == one_list[8] == "1" or \
    one_list[2] == one_list[4] == one_list[6] == "1":
    print("First player won")
elif one_list[0] == one_list[1] == one_list[2] == "2" or \
        one_list[3] == one_list[4] == one_list[5] == "2" or \
        one_list[6] == one_list[7] == one_list[8] == "2" or \
        one_list[0] == one_list[3] == one_list[6] == "2" or \
        one_list[1] == one_list[4] == one_list[7] == "2" or \
        one_list[2] == one_list[5] == one_list[8] == "2" or \
        one_list[0] == one_list[4] == one_list[8] == "2" or \
        one_list[2] == one_list[4] == one_list[6] == "2":
    print("Second player won")
else:
    print("Draw")
