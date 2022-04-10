def computer_store():
    total_wo_tax = 0
    while True:
        parts = input()
        if parts == "special" or parts == "regular":
            break
        if float(parts) >= 0:
            total_wo_tax += float(parts)
        else:
            print("Invalid price!")
    tax = total_wo_tax * 0.2
    total_with_tax = total_wo_tax + tax

    if total_with_tax != 0:
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_wo_tax:.2f}$")
        # print(f"{total_wo_tax:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print("-----------")
        if parts == "special":
            print(f"Total price: {total_with_tax - (total_with_tax * 0.1) :.2f}$")
        elif parts == "regular":
            print(f"Total price: {total_with_tax:.2f}$")
    else:
        print("Invalid order!")


computer_store()
