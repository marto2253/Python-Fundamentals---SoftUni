def phonebook(seq):
    contact_book = dict()

    while "-" in seq:
        info = seq.split("-")
        name = info[0]
        number = info[1]

        contact_book[name] = number

        seq = input()

    seq = int(seq)
    for i in range(seq):
        name_search = input()
        if name_search in contact_book.keys():
            print(f"{name_search} -> {contact_book[name_search]}")
        else:
            print(f"Contact {name_search} does not exist.")


sequence = input()
phonebook(sequence)