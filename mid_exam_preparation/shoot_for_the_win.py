sequence = list(map(int, input().split(" ")))
command = input()
shot_targets = 0

while command != "End":
    index = int(command)
    if index in range(len(sequence)):
        current_value = sequence[index]
        sequence[index] = -1
        for i in range(len(sequence)):
            if current_value < sequence[i] != -1:
                sequence[i] -= current_value
            elif current_value >= sequence[i] != -1:
                sequence[i] += current_value
        shot_targets += 1

    command = input()
print(f"Shot targets: {shot_targets} -> {' '.join([str(i) for i in sequence])} ")
