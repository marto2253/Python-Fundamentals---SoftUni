# import sys

sequence = input().split(" ")
number = int(input())

sequence_int = [int(i) for i in sequence]
# sorted_sequence_int = sorted(([int(i) for i in sequence]), reverse=True)
#
# counter = 0
# min_number = -sys.maxsize
#
# for i in range(len(sorted_sequence_int) -1, -1, -1):
#     if counter == number:
#         break
#     if sorted_sequence_int[i] > min_number:
#         min_number = sorted_sequence_int[i]
#         sorted_sequence_int.pop()
#     counter += 1
#
# for i in range(len(sequence_int) -1, -1, -1):
#     if sequence_int[i] not in sorted_sequence_int:
#         sequence_int.remove(sequence_int[i])

for i in range(number):
    x = min(sequence_int)
    sequence_int.remove(x)

string_sequence_int = [str(i) for i in sequence_int]
print(", ".join(string_sequence_int))
