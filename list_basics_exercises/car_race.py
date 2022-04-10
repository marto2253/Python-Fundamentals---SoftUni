sequence = input()

sequence_list = sequence.split(" ")
stop = len(sequence_list) // 2

counter = 0
left_car_time = 0
right_car_time = 0

for i in range(len(sequence_list) // 2):  # starting from left side
    if sequence_list[i] == "0":
        left_car_time *= 0.8
    else:
        left_car_time += float(sequence_list[i])

for x in range(len(sequence_list)-1, -1, -1):  # starting from right side
    if counter == stop:
        break
    if sequence_list[x] == "0":
        right_car_time *= 0.8
    else:
        right_car_time += float(sequence_list[x])
    counter += 1

if left_car_time < right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
else:
    print(f'The winner is right with total time: {right_car_time:.1f}')
