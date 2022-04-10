# import math

number_of_people = int(input())
capacity = int(input())

if capacity > number_of_people:
    courses = 1
else:
    courses = (number_of_people // capacity) + (number_of_people & capacity)

# courses = number_of_people / capacity

# print(math.ceil(courses))
print(courses)