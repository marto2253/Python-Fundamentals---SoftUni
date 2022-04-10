def change_side(book_dict, left_side, right_side):
    for current_side in book_dict:
        if right_side in book_dict[current_side]:
            if len(book_dict[right_side]) > 1:
                book_dict[current_side].pop(left_side)
                break
            else:
                del book_dict[current_side]
                break

    if right_side in book_dict:
        book_dict[right_side].append(left_side)
    else:
        book_dict[right_side] = [left_side]

    print(f"{left_side} joins the {right_side} side!")


def force_book(seq):
    book_dict = dict()
    while seq != "Lumpawaroo":
        if "|" in seq:
            info = seq.split(" | ")
            left_side = info[0]
            right_side = info[1]
            if left_side not in book_dict:
                book_dict[left_side] = list()
                if right_side not in book_dict.values():
                    book_dict[left_side].append(right_side)
        elif '->' in seq:
            info = seq.split(" -> ")
            left_side = info[0]
            right_side = info[1]
            change_side(book_dict, left_side, right_side)

        seq = input()
    print(book_dict)
    for k, v in book_dict.items():
        if len(book_dict[k]) != 0:
            print(f"Side: {k}, Members: {len(v)}")
            values = '\n! '.join(v)
            print(f"! {values}")


sequence = input()
force_book(sequence)