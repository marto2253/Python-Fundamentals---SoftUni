placed_orders = int(input())
total = 0

for i in range(placed_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    placed_order_total = price_per_capsule * days * capsule_count
    total += placed_order_total

    print(f"The price for the coffee is: ${placed_order_total:.2f}")

print(f"Total: ${total:.2f}")