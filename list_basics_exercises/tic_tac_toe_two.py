line_one = input().split(" ")
line_two = input().split(" ")
line_three = input().split(" ")

one_list = [line_one, line_two, line_three]

counter_one = 0
counter_two = 0

for first_list in one_list:
    for x in first_list:
        if x == "1":
            counter_one += 1
        if x == "2":
            counter_two += 1

if counter_one == 3 and counter_two != 3:
    print("First player won")
elif counter_two == 3 and counter_one != 3:
    print("Second player won")
elif counter_one and counter_two == 3:
    print("Draw!")
