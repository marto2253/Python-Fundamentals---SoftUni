def office_chairs(rooms):
    free_chairs = 0
    less_chairs = False
    for i in range(rooms):
        room_info = input().split(" ")
        chairs = room_info[0]
        people = int(room_info[1])

        if len(chairs) >= people:
            free_chairs += len(chairs) - people
            continue
        elif len(chairs) < people:
            less_chairs = True
            print(f"{people - len(chairs)} more chairs needed in room {i + 1}")

    if not less_chairs:
        print(f"Game On, {free_chairs} free chairs left")


number_of_rooms = int(input())
office_chairs(number_of_rooms)
