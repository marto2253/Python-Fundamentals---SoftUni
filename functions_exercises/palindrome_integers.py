def palindrome(seq):
    for i in seq:
        if int(i) == int(i[::-1]):
            print("True")
        else:
            print("False")


sequence = input().split(", ")
palindrome(sequence)
