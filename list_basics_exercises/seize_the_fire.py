cells = input().replace(" = ", ":").replace("#", ":").split(":")
amount_of_water = int(input())
total_fire = 0
chuncked_list = list()
put_out_cells = []

for i in range(0, len(cells), 2):
    chuncked_list.append(cells[i:i+2])

for i in chuncked_list:
    value = int(i[1])
    if i[0] == "High":
        if 81 <= value <= 125:
            if amount_of_water - value >= 0:
                amount_of_water -= value
                put_out_cells.append(value)
                total_fire += value

    if i[0] == "Medium":
        if 51 <= value <= 80:
            if amount_of_water - value >= 0:
                amount_of_water -= value
                put_out_cells.append(value)
                total_fire += value

    if i[0] == "Low":
        if 1 <= value <= 50:
            if amount_of_water - value >= 0:
                amount_of_water -= value
                put_out_cells.append(value)
                total_fire += value

effort = total_fire * 0.25
print("Cells:")
for i in put_out_cells:
    print(f" - {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")