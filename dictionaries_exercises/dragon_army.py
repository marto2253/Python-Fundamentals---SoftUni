def dragon_army(iters):
    dragons = {}
    default_health = 250
    default_damage = 45
    default_armor = 10
    condition = False

    for i in range(iters):
        sequence = input()
        sequence = sequence.split(" ")
        type_d = sequence[0]
        name = sequence[1]
        damage = sequence[2]
        health = sequence[3]
        armor = sequence[4]

        if type_d not in dragons:
            dragons[type_d] = {}
            condition = True
        else:
            if name in dragons[type_d]:
                condition = True
            else:
                condition = True

        if condition:
            if damage != 'null' and health != 'null' and armor != 'null':
                dragons[type_d][name] = int(damage), int(health), int(armor)
            if damage == 'null':
                dragons[type_d][name] = int(default_damage)
            if health == 'null':
                dragons[type_d][name] = int(default_health)
            if armor == 'null':
                dragons[type_d][name] = int(default_armor)

    for k, v in dragons.items():
        sort_names = dict(sorted(v.items(), key=lambda x: x[0]))
        average_damage = 0
        average_health = 0
        average_armor = 0
        counter = 0
        for stats in v.values():
            counter += 1
            average_damage += stats[0]
            average_health += stats[1]
            average_armor += stats[2]
        print(f'{k}::({average_damage/counter:.2f}/{average_health/counter:.2f}/{average_armor/counter:.2f})')
        for na, st in sort_names.items():
            print(f'-{na} -> damage: {st[0]}, health: {st[1]}, armor: {st[2]}')


num_of_iters = int(input())
dragon_army(num_of_iters)
