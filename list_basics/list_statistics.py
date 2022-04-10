iterations = int(input())

positive = list()
negative = list()

for i in range(iterations):
    numbers = int(input())
    if numbers >= 0:
        positive.append(numbers)
    else:
        negative.append(numbers)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
