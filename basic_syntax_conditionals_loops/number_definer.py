number = float(input())
abs_number = abs(number)

if number == 0:
    print("zero")
elif number < 0:
    if abs_number < 1 and abs_number != 0:
        print("small negative")
    elif abs_number > 1000000:
        print("large negative")
    else:
        print("negative")
elif number > 0:
    if abs_number > 1000000:
        print("large positive")
    elif abs_number < 1 and abs_number != 0:
        print("small positive")
    else:
        print("positive")