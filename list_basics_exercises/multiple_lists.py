factor = int(input())
count = int(input())

length_list = list()

for i in range(factor, count * factor + 1, factor):
    length_list.append(i)

print(length_list)

