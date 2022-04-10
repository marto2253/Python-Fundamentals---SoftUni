def factorial_division(n1, n2):
    sum1 = 1
    sum2 = 1
    for num in range(1, n1+1):
        sum1 *= num
    for num in range(1, n2+1):
        sum2 *= num

    return f"{sum1/sum2:.2f}"


number1 = int(input())
number2 = int(input())

print(factorial_division(number1, number2))