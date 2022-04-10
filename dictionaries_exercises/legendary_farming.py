def legendary_farming(seq):
    materials = {'fragments': 0, 'shards': 0, 'motes': 0}
    condition = False
    special_item = ''
    while True:
        pairs = [seq[i:i + 2] for i in range(0, len(seq), 2)]
        for i in pairs:
            name = i[1]
            quantity = int(i[0])

            if name not in materials:
                materials[name] = quantity
            else:
                materials[name] += quantity

            if materials[name] >= 250:
                materials[name] -= 250
                condition = True
                if name == "fragments":
                    special_item += 'Valanyr'
                if name == "shards":
                    special_item += 'Shadowmourne'
                if name == "motes":
                    special_item += 'Dragonwrath'
                break
        if condition:
            break
        seq = input().lower().split(" ")

    print(f"{special_item} obtained!")
    print(f'shards: {materials["shards"]}')
    print(f'fragments: {materials["fragments"]}')
    print(f'motes: {materials["motes"]}')

    for k, v in materials.items():
        if k != 'shards' and k != 'fragments' and k != 'motes':
            print(f'{k}: {v}')


sequence = input().lower().split(" ")
legendary_farming(sequence)
