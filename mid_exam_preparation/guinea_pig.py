quantity_food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
break_con = False

for i in range(1, 31):
    if hay <= 0 or cover <= 0 or quantity_food <= 0:
        print("Merry must go to the pet store!")
        break_con = True
        break
    quantity_food -= 0.3 * 1000
    if i % 2 == 0:
        hay -= quantity_food * 0.05
    if i % 3 == 0:
        cover -= weight / 3

if quantity_food > 0:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
elif quantity_food <= 0 and not break_con:
    print("Merry must go to the pet store!")
