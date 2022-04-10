def pirates(seq):

    pirate_crew = {}

    while seq != 'Sail':
        seq = seq.split("||")
        city = seq[0]
        population = int(seq[1])
        gold = int(seq[2])

        if city not in pirate_crew:
            pirate_crew[city] = [population, gold]
        else:
            pirate_crew[city][0] += population
            pirate_crew[city][1] += gold

        seq = input()

    event = input()

    while event != 'End':
        event = event.split('=>')
        action = event[0]

        if action == 'Plunder':
            city = event[1]
            people = int(event[2])
            gold = int(event[3])

            pirate_crew[city][0] -= people
            pirate_crew[city][1] -= gold
            print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

            if pirate_crew[city][0] <= 0 or pirate_crew[city][1] <= 0:
                del pirate_crew[city]
                print(f"{city} has been wiped off the map!")

        elif action == 'Prosper':
            city = event[1]
            gold = int(event[2])

            if gold < 0:
                print(f"Gold added cannot be a negative number!")
            else:
                pirate_crew[city][1] += gold
                print(f"{gold} gold added to the city treasury. {city} now has {pirate_crew[city][1]} gold.")

        event = input()

    if len(pirate_crew) > 0:
        print(f"Ahoy, Captain! There are {len(pirate_crew)} wealthy settlements to go to:")
        for k, v in pirate_crew.items():
            print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


sequence = input()
pirates(sequence)
