import sys

number_of_snowballs = int(input())
highest_value = -sys.maxsize

current_weight = 0
current_time_required = 0
current_quality = 0

for i in range(number_of_snowballs):
    weight = int(input())
    time_required = int(input())
    quality = int(input())

    value_per_ball = (weight / time_required) ** quality
    if value_per_ball > highest_value:
        highest_value = int(value_per_ball)
        current_weight = weight
        current_time_required = time_required
        current_quality = quality


print(f'{current_weight} : {current_time_required} = {highest_value} ({current_quality})')
