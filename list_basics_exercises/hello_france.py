bought_items = input().replace("->", " ").replace("|", " ").split(" ")
budget = int(input())
current_budget = budget

item_price = list()
item_bought_total = []

after_selling = 0

for i in range(0, len(bought_items), 2):
    item_price.append(bought_items[i:i+2])

for pair in item_price:
    value_of_item = float(pair[1])
    if pair[0] == "Clothes":
        if value_of_item <= 50.00:
            if current_budget >= value_of_item:
                current_budget -= value_of_item
                item_bought_total.append(value_of_item)
    if pair[0] == "Shoes":
        if value_of_item <= 35.00:
            if current_budget >= value_of_item:
                current_budget -= value_of_item
                item_bought_total.append(value_of_item)
    if pair[0] == "Accessories":
        if value_of_item <= 20.50:
            if current_budget >= value_of_item:
                current_budget -= value_of_item
                item_bought_total.append(value_of_item)

after_selling = sum(item_bought_total) + (sum(item_bought_total) * 0.4)

for i in range(len(item_bought_total)):
    print(f"{item_bought_total[i] + (item_bought_total[i] * 0.4):.2f}", end=" ")

print(f"\nProfit: {after_selling - budget + current_budget:.2f}")
if current_budget + after_selling > 150:
    print("Hello, France!")
else:
    print("Not enough money.")

