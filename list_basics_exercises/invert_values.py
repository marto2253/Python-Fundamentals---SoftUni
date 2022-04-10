# sequence = input().split(" ")
# inverted_values = list()

# for i in sequence:
#     if int(i) >= 0:
#         inverted_values.append(-int(i))
#     else:
#         inverted_values.append(abs(int(i)))
#
# print(inverted_values)

a = [-num for num in list(map(int, input().split(" ")))]
print(a)

