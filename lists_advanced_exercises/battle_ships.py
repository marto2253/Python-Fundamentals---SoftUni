def battle_ships(rows):
    field_rows = []
    destroyed_ships = 0

    for i in range(rows):
        field_rows.append(list(map(int, input().split(" "))))

    attacks = list(map(str, input().split(" ")))

    for i in attacks:
        counter2 = 0
        column = int(i[2])
        if int(i[0]) == 0:
            for row in field_rows:
                if counter2 == int(i[0]):
                    row[column] -= 1
                    if row[column] == 0:
                        destroyed_ships += 1
                counter2 += 1
        elif int(i[0]) == 1:
            for row in field_rows:
                if counter2 == int(i[0]):
                    row[column] -= 1
                    if row[column] == 0:
                        destroyed_ships += 1
                counter2 += 1
        elif int(i[0]) == 2:
            for row in field_rows:
                if counter2 == int(i[0]):
                    row[column] -= 1
                    if row[column] == 0:
                        destroyed_ships += 1
                counter2 += 1
        elif int(i[0]) == 3:
            for row in field_rows:
                if counter2 == int(i[0]):
                    row[column] -= 1
                    if row[column] == 0:
                        destroyed_ships += 1
                counter2 += 1

    print(destroyed_ships)


rows_input = int(input())
battle_ships(rows_input)
