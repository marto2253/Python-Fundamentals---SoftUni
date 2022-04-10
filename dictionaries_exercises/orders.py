def orders(seq):

    dictionary = dict()

    while seq != "buy":
        info = seq.split(" ")
        product = info[0]
        price = float(info[1])
        quantity = int(info[2])

        if product not in dictionary:
            dictionary[product] = list()
            dictionary[product].append(price)
            dictionary[product].append(quantity)
        else:
            dictionary[product][0] = price
            dictionary[product][1] += quantity

        seq = input()

    for k, v in dictionary.items():
        print(f"{k} -> {v[0] * v[1]:.2f}")


sequenece = input()
orders(sequenece)
