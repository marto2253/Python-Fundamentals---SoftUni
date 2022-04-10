sequence = input().split(" ")

counter_A_team = 11
counter_B_team = 11

all_players = []

for i in sequence:
    if i not in all_players:
        all_players.append(i)

for i in all_players:
    if i[0] == "A":
        counter_A_team -= 1
        if counter_A_team < 7:
            break
    else:
        counter_B_team -= 1
        if counter_B_team < 7:
            break

print(f"Team A - {counter_A_team}; Team B - {counter_B_team}")
if counter_A_team < 7 or counter_B_team < 7:
    print("Game was terminated")