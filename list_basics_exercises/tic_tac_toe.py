line_one = input()
line_two = input()
line_three = input()

x = line_one.split(" ")
x2 = line_two.split(" ")
x3 = line_three.split(" ")

x.extend(x2)
x.extend(x3)

counter_one = 0
counter_two = 0

while True:
    for i in x:
        if i == "0":
            x.remove(i)
    break

is_Draw = True

for y in x:
    if y == "1":
        counter_one += 1
        counter_two = 0
        if counter_one == 3:
            print("First player won")
            is_Draw = False
            break
    if y == "2":
        counter_two += 1
        counter_one = 0
        if counter_two == 3:
            print("Second player won")
            is_Draw = False
            break

if is_Draw:
    print("Draw!")

