iterations = int(input())
sum = 0

for i in range(iterations):
    letters = input()
    sum += ord(letters)

print(f"The sum equals: {sum}")
