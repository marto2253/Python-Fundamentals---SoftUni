key = int(input())
number_of_lines = int(input())

message = ""
addition = 0

for i in range(number_of_lines):
    letter = input()
    addition = ord(letter) + key
    message += chr(addition)

print(message)