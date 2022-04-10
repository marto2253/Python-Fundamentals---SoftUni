def perfect_number(num):
    comment = 0
    for i in range(1, num):
        if int(num) % i == 0:
            comment += i

    if comment == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

number = int(input())

perfect_number(number)
