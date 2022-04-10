def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(number)):
        current_number = int(number[i])
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


single_number = input()

print(odd_even_sum(single_number))