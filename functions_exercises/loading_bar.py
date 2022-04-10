def loading_bar(n):
    divided = n // 10
    dots = 10 - divided
    if divided == 10:
        print(f"{n}% Complete!\n"
              f"[{'%' * divided}]")
    else:
        print(f"{n}% [{'%' * divided}{'.' * dots}]\n"
              f"Still loading...")


number = int(input())

loading_bar(number)