numbers = list(map(int, input().split(', ')))

positive = []
negative = []
odd = []
even = []

for i in numbers:
    if i >= 0:
        positive.append(str(i))
    if i < 0:
        negative.append(str(i))
    if i % 2 == 0:
        even.append(str(i))
    if i % 2 != 0:
        odd.append(str(i))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
