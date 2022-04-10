number = int(input())

even = list()
odd = list()
negative = list()
positive = list()

for i in range(number):
    integers = int(input())
    if integers >= 0:
        positive.append(integers)
    else:
        negative.append(integers)
    if integers % 2 == 0:
        even.append(integers)
    else:
        odd.append(integers)

command = input()
print(eval(command))
