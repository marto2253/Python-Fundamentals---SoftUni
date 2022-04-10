def snow_white(seq):
    dwarves = dict()

    while seq != 'Once upon a time':
        seq = seq.split(" <:> ")
        name = seq[0]
        hat = seq[1]
        points = int(seq[2])

        if name not in dwarves:
            dwarves[name] = {}
            dwarves[name][hat] = points
        else:
            if hat not in dwarves[name]:
                dwarves[name][hat] = points
            if points > dwarves[name][hat]:
                dwarves[name][hat] = points

        seq = input()

    for k, v in dwarves.items():
        sort_values = dict(sorted(v.items(), key=lambda x: -x[1]))
        for k1, v1 in sort_values.items():
            print(k1, k, v1)


sequence = input()
snow_white(sequence)
