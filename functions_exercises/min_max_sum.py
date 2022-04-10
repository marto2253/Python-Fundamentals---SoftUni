def min_max_sum(num_seq):
    minimum = min(num_seq)
    maximum = max(num_seq)
    total = sum(num_seq)

    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {total}")


sequence = [int(i) for i in input().split(" ")]

min_max_sum(sequence)
