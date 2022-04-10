number_of_lines = int(input())

counter = 0

for i in range(number_of_lines):
    random_input = input()
    if random_input == "(":
        counter += 1
    if random_input == ")":
        counter -= 1
        # break

if counter != 0:
    print("UNBALANCED")
else:
    print("BALANCED")
