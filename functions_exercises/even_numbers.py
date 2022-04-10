def even_numbers(num):
    if int(num) % 2 == 0:
        return True

sequence = input().split(" ")
filtered = filter(even_numbers, sequence)
even_numbers_list = list()

for i in filtered:
    even_numbers_list.append(int(i))

print(even_numbers_list)