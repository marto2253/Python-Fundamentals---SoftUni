year = int(input())

is_Happy_Year = False

while not is_Happy_Year:
    year += 1
    new_set = set(str(year))

    is_Happy_Year = len(str(year)) == len(new_set)

print(f"{year}")

