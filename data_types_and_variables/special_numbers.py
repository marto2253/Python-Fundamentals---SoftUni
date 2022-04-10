number = int(input())

for i in range(1, number + 1):
    sum_of_digits = 0
    digits = i
    while digits > 0:
        sum_of_digits += digits % 10
        print(sum_of_digits)
        digits = int(digits / 10)
        print(digits)

    is_Special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    print(f'{i} -> {is_Special}')
