sequence_one = input().split(", ")
sequence_two = input().split(", ")

# list_strings = list()
#
# for i in sequence_one:
#     if str(i) in str(sequence_two):
#         list_strings.append(i)

list_strings = [str(i) for i in sequence_one if i in str(sequence_two)]

print(list_strings)
