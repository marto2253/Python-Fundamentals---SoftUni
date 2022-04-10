def statistics(pairs):
    dictionary = dict()

    while pairs != "statistics":
        pairs_split = pairs.split(": ")
        product = pairs_split[0]
        quantity = int(pairs_split[1])

        if product not in dictionary.keys():
            dictionary[product] = quantity
        else:
            dictionary[product] += quantity

        pairs = input()

    print("Products in stock:")
    for keys, values in dictionary.items():
        print(f"- {keys}: {values}")
    print(f"Total Products: {len(dictionary.keys())}")
    print(f"Total Quantity: {sum(dictionary.values())}")


pairs = input()
statistics(pairs)
