def pass_validator(password):
    length = False
    let_digits = False
    two_digits = False
    counter = 0
    if 6 <= len(password) <= 10:
        length = True
    if password.isalnum():
        let_digits = True
    for i in range(len(password)):
        if password[i].isdigit():
            counter += 1
            if counter == 2:
                two_digits = True
    if length == let_digits == two_digits:
        print("Password is valid")
    if not length:
        print("Password must be between 6 and 10 characters")
    if not let_digits:
        print("Password must consist only of letters and digits")
    if not two_digits:
        print("Password must have at least 2 digits")


password = input()
pass_validator(password)