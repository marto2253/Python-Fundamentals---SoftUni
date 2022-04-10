import math


def center_point(n1, n2, n3, n4):

    if (abs(n1), abs(n2)) <= (abs(n3), abs(n4)):
        return f"({math.floor(n1)}, {math.floor(n2)})"
    else:
        return f"({math.floor(n3)}, {math.floor(n4)})"


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

print(center_point(num1, num2, num3, num4))
