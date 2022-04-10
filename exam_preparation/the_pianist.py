def pianist(num):
    fav_pieces = dict()
    for _ in range(num):
        seq = input().split('|')
        piece = seq[0]
        composer = seq[1]
        key = seq[2]

        fav_pieces[piece] = [composer, key]

    command = input()

    while command != 'Stop':

        command = command.split('|')

        if command[0] == 'Add':
            piece = command[1]
            composer = command[2]
            key = command[3]

            if piece in fav_pieces:
                print(f"{piece} is already in the collection!")
            else:
                fav_pieces[piece] = [composer, key]
                print(f"{piece} by {composer} in {key} added to the collection!")

        elif command[0] == 'Remove':
            piece = command[1]

            if piece in fav_pieces:
                del fav_pieces[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

        elif command[0] == 'ChangeKey':
            piece = command[1]
            key = command[2]

            if piece in fav_pieces:
                fav_pieces[piece][1] = key
                print(f"Changed the key of {piece} to {key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

        command = input()

    for k, v in fav_pieces.items():
        print(f"{k} -> Composer: {v[0]}, Key: {v[1]}")


number = int(input())
pianist(number)