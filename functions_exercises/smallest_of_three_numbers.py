import sys

def smallest_number(n1, n2, n3):
    max_number = sys.maxsize
    if n1 < max_number:
        max_number = n1
    if n2 < max_number:
        max_number = n2
    if n3 < max_number:
        max_number = n3
    return max_number

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(smallest_number(n1, n2, n3))