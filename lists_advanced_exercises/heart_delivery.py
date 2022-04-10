houses = [int(i) for i in input().split("@")]

command = input()
index = 0

while command != "Love!":
    split_command = command.split(" ")
    jump = split_command[0]
    length = int(split_command[1])
    if jump == "Jump":
        index += length
        if length in range(len(houses)) and index in range(len(houses)):
            if houses[index] != 0:
                houses[index] -= 2
                if houses[index] == 0:
                    print(f"Place {index} has Valentine's day.")
            else:
                print(f"Place {index} already had Valentine's day.")
        else:
            if houses[0] != 0:
                houses[0] -= 2
                if houses[0] == 0:
                    print(f"Place 0 has Valentine's day.")
            else:
                print(f"Place 0 already had Valentine's day.")
            index = 0

    command = input()

print(f"Cupid's last position was {index}.")
failed = [i for i in houses if i != 0]
if len(failed) != 0:
    print(f"Cupid has failed {len(failed)} places.")
else:
    print("Mission was successful.")
