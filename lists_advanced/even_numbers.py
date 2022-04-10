numbers = list(map(int, input().split(", ")))

even_number_indexes = list()

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_number_indexes.append(i)

print(even_number_indexes)
