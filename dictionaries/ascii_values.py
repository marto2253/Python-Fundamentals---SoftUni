# def ascii_values(seq):
#     dictionary = dict()
#     for i in seq:
#         dictionary[i] = ord(i)
#     return dictionary
#
#
# sequence = input().split(", ")
# print(ascii_values(sequence))

print({i:ord(i) for i in input().split(", ")})