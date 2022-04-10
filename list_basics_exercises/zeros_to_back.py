string = input()

first_list = string.split(", ")

zeroes = []
other = []

for i in first_list:
    if i == str(0):
        zeroes.append(int(i))
    else:
        other.append(int(i))

other.extend(zeroes)

print(other)
