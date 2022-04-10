days_of_adventure = int(input())
count_players = int(input())
group_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
total_water = water_per_day * days_of_adventure * count_players
total_food = food_per_day * days_of_adventure * count_players

for i in range(1, days_of_adventure + 1):
    energy_lost = float(input())
    if group_energy - energy_lost <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break
    else:
        group_energy -= energy_lost
    if i % 2 == 0:
        group_energy += group_energy * 0.05
        total_water -= total_water * 0.3
    if i % 3 == 0:
        total_food -= total_food / count_players
        group_energy += group_energy * 0.1
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
