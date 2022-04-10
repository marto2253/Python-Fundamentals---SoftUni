def plant_discovery(num):

    plants = {}

    for i in range(num):
        plants_info = input().split('<->')
        name = plants_info[0]
        rarity = int(plants_info[1])

        if name not in plants:
            plants[name] = [rarity]
        else:
            plants[name][0] = rarity

    commands = input()

    while commands != 'Exhibition':

        commands = commands.split(': ')

        action = commands[0]

        if action == 'Rate':
            additional_commands = commands[1].split(' - ')
            plant = additional_commands[0]
            rating = int(additional_commands[1])

            if plant in plants:
                plants[plant].append(rating)
            else:
                print('error')

        elif action == 'Update':
            additional_commands = commands[1].split(' - ')
            plant = additional_commands[0]
            new_rarity = int(additional_commands[1])

            if plant in plants:
                plants[plant][0] = new_rarity
            else:
                print('error')

        elif action == 'Reset':
            additional_commands = commands[1].split(' - ')
            plant = additional_commands[0]

            if plant in plants:
                del plants[plant][1:]
            else:
                print('error')

        commands = input()

    print('Plants for the exhibition:')
    for k, v in plants.items():
        if len(v) > 1:
            sum_of_values = sum(v) - v[0]
            length_of_values = len(v) - 1
            print(f"- {k}; Rarity: {v[0]}; Rating: {sum_of_values/length_of_values:.2f}")
        else:
            print(f"- {k}; Rarity: {v[0]}; Rating: {0:.2f}")


number = int(input())
plant_discovery(number)
