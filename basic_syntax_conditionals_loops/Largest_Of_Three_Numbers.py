import sys

biggest_number = -sys.maxsize

for i in range(3):
    n = int(input())
    if n > biggest_number:
        biggest_number = n

print(biggest_number)

