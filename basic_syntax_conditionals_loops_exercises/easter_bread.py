budget = float(input())
price_flour_kg = float(input())

bread_counter = 0
current_bread_counter = 0
colored_eggs_counter = 0

price_pack_eggs = price_flour_kg * 0.75
price_litre_milk = price_flour_kg + (price_flour_kg * 0.25)
price_quater_milk = price_litre_milk * 0.25

one_bread_price = price_flour_kg + price_pack_eggs + price_quater_milk

total = 0
current_total = 0

while True:
    total += one_bread_price
    if budget < total:
        break
    bread_counter += 1
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        current_bread_counter += bread_counter - 2
    current_total += one_bread_price

remaining_budget = budget - current_total
total_colored_eggs = colored_eggs_counter - current_bread_counter

print(f"You made {bread_counter} loaves of Easter bread! Now you have {total_colored_eggs} eggs and {remaining_budget:.2f}BGN left.")
