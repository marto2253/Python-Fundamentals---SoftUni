n_of_iterations = int(input())
word = input()

string_list = list()
filter = list()

for i in range(n_of_iterations):
    string = input()
    string_list.append(string)
    if word in string:
        filter.append(string)

print(string_list)
print(filter)