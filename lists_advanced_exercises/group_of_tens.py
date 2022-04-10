number_sequence = list(map(int, input().split(", ")))

boundary = 0

while len(number_sequence) != 0:
    current_list = list()
    boundary += 10
    for i in range(len(number_sequence) -1, -1, -1):
        if boundary - 10 < number_sequence[i] <= boundary:
            current_list.append(number_sequence[i])
            number_sequence.remove(number_sequence[i])
    else:
        print(f"Group of {boundary}'s: {current_list[::-1]}")
        current_list.clear()
