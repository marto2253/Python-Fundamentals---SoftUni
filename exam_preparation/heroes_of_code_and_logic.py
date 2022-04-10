def heroes_of_code(iters):

    heroes = {}

    max_mp = 200
    max_hp = 100

    for _ in range(iters):
        heroes_details = input().split()
        name = heroes_details[0]
        hp = int(heroes_details[1])
        mp = int(heroes_details[2])

        heroes[name] = [hp, mp]

    commands = input()

    while commands != "End":
        commands = commands.split(" - ")
        action = commands[0]
        hero_name = commands[1]

        if action == 'CastSpell':
            mp_needed = int(commands[2])
            spell_name = commands[3]

            if heroes[hero_name][1] >= mp_needed:
                heroes[hero_name][1] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif action == 'TakeDamage':
            damage = int(commands[2])
            attacker = commands[3]

            if heroes[hero_name][0] > damage:
                heroes[hero_name][0] -= damage
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
            else:
                print(f"{hero_name} has been killed by {attacker}!")
                del heroes[hero_name]

        elif action == 'Recharge':
            amount = int(commands[2])
            if heroes[hero_name][1] + amount > 200:
                print(f"{hero_name} recharged for {max_mp - heroes[hero_name][1]} MP!")
                heroes[hero_name][1] = max_mp
            else:
                heroes[hero_name][1] += amount
                print(f"{hero_name} recharged for {amount} MP!")

        elif action == 'Heal':
            amount = int(commands[2])
            if heroes[hero_name][0] + amount > 100:
                print(f"{hero_name} healed for {max_hp - heroes[hero_name][0]} HP!")
                heroes[hero_name][0] = max_hp
            else:
                heroes[hero_name][0] += amount
                print(f"{hero_name} healed for {amount} HP!")

        commands = input()

    for k, v in heroes.items():
        print(k)
        print(f'  HP: {v[0]}')
        print(f'  MP: {v[1]}')


iterations = int(input())
heroes_of_code(iterations)