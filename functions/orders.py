def total_price(item, quantity):
    if item == "coffee":
        return quantity * 1.50
    elif item == "coke":
        return quantity * 1.40
    elif item == "water":
        return quantity * 1
    elif item == "snacks":
        return quantity * 2


current_item = input()
current_quantity = int(input())

print(f"{total_price(current_item, current_quantity):.2f}")