def stock(seq, p_s):
    products_dict = dict()

    for i in range(0, len(seq), 2):
        food = seq[i]
        quantity = seq[i+1]
        products_dict[food] = int(quantity)

    for i in p_s:
        if i in products_dict.keys():
            print(f'We have {products_dict[i]} of {i} left')
        else:
            print(f"Sorry, we don't have {i}")


sequence = input().split(" ")
products_search = input().split(" ")

stock(sequence, products_search)

