number = int(input())

for i in range(number):
    for x in range(number):
        for y in range(number):
            print(f"{chr(97 + i)}{chr(97 + x)}{chr(97 + y)}")