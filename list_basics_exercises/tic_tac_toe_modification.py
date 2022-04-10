line_one = input()
line_two = input()
line_three = input()

split_line_one = line_one.split(" ")
split_line_two = line_two.split(" ")
split_line_three = line_three.split(" ")

one_list = [split_line_one + split_line_two + split_line_three]

counter_one = 0
counter_two = 0

while True:
    for i in one_list:
        if i == "0":
            one_list.remove(i)
    break

for y in one_list:
    for x in y:
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
