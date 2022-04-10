def game(num):

    cars = dict()

    for _ in range(num):

        car_info = input().split('|')
        car = car_info[0]
        mileage = int(car_info[1])
        fuel = int(car_info[2])

        cars[car] = [mileage, fuel]

    commands = input()

    while commands != 'Stop':

        commands = commands.split(' : ')

        action = commands[0]
        car = commands[1]

        if action == 'Drive':
            distance = int(commands[2])
            fuel = int(commands[3])

            if fuel > cars[car][1]:
                print('Not enough fuel to make that ride')
            else:
                if cars[car][0] + distance < 100000:
                    print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
                    cars[car][0] += distance
                    cars[car][1] -= fuel
                else:
                    print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
                    print(f"Time to sell the {car}!")
                    del cars[car]

        elif action == 'Refuel':
            fuel = int(commands[2])
            if cars[car][1] + fuel > 75:
                print(f"{car} refueled with {75 - cars[car][1]} liters")
                cars[car][1] = 75
            else:
                cars[car][1] += fuel
                print(f"{car} refueled with {fuel} liters")

        elif action == 'Revert':
            km = int(commands[2])

            if cars[car][0] - km < 10000:
                cars[car][0] = 10000
            else:
                cars[car][0] -= km
                print(f"{car} mileage decreased by {km} kilometers")

        commands = input()

    for k, v in cars.items():
        print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")


number = int(input())
game(number)
