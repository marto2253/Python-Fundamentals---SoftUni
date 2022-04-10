def judge(seq):
    users = {}
    individual = {}

    while seq != "no more time":
        seq = seq.split(" -> ")
        user_name = seq[0]
        contest = seq[1]
        points = int(seq[2])
        if contest in users:
            if user_name in users[contest]:
                if users[contest][user_name] < points:
                    users[contest][user_name] = points
                    individual[user_name] = points

            else:
                users[contest][user_name] = points
                if user_name in individual:
                    individual[user_name] += points
                else:
                    individual[user_name] = points
        else:
            users[contest] = {}
            users[contest][user_name] = points
            if user_name in individual:
                individual[user_name] += points
            else:
                individual[user_name] = points

        seq = input()

    i = 0
    for k, v in users.items():
        print(f'{k}: {len(users[k])} participants')
        sorted_values = dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
        for keys, values in sorted_values.items():
            i += 1
            print(f"{i}. {keys} <::> {values}")
        i = 0
    print("Individual standings:")
    sorted_individual = dict(sorted(individual.items(), key=lambda x: (-x[1], x[0])))
    for k, v in sorted_individual.items():
        i += 1
        print(f"{i}. {k} -> {v}")


sequence = input()
judge(sequence)
