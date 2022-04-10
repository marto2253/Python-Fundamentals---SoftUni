iterations = int(input())
capacity = 255
new_capacity = 0

# for i in range(iterations):
#     liters_water = int(input())
#     if liters_water + new_capacity < capacity:
#         new_capacity += liters_water
#     else:
#         print("Insufficient capacity!")

for i in range(iterations):
    liters_water = int(input())
    new_capacity += liters_water
    if new_capacity > 255:
        print("Insufficient capacity!")
        new_capacity -= liters_water

print(new_capacity)
