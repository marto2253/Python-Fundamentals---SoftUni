addition = 0

for i in range(1, 5):
    number = int(input())
    if i == 1 or i == 2:
        addition += number
    if i == 3:
        addition //= number
    if i == 4:
        addition *= number

print(addition)