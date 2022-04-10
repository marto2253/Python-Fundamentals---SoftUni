# names = [i for i in input().split(", ")]
#
# sorted_names = sorted(names, key= lambda x: (-len(x), x))
#
# print(sorted_names)

names = sorted([i for i in input().split(", ")], key= lambda x: (-len(x), x))

print(names)