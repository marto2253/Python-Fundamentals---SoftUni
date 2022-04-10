divisor = int(input())
boundry = int(input())
# N = ""
#
# for i in range(1, boundry + 1):
#     multiplication = divisor * i
#     if multiplication > boundry:
#         break
#     else:
#         N = multiplication
#
# print(N)


result = int(boundry / divisor) * divisor
print(result)