import sys


def ranking(seq):

    courses = dict()
    users_info = {}
    while seq != "end of contests":
        seq = seq.split(":")
        course = seq[0]
        password = seq[1]
        courses[course] = {}
        courses[course][password] = 0

        seq = input()

    seq2 = input()
    while seq2 != "end of submissions":
        seq2 = seq2.split("=>")
        c = seq2[0]
        p = seq2[1]
        user = seq2[2]
        points = int(seq2[3])
        if user not in users_info and c in courses and p in courses[c]:
            users_info[user] = {}
            users_info[user][c] = points
        elif user in users_info and c in courses and p in courses[c]:
            if c in users_info[user]:
                if users_info[user][c] < points:
                    users_info[user][c] = points
            else:
                users_info[user][c] = points

        seq2 = input()

    max_points = -sys.maxsize
    best_candidate = ''
    for name in users_info:
        current_points = 0
        for cc in users_info[name]:
            current_points += users_info[name][cc]
        if current_points > max_points:
            max_points = current_points
            best_candidate += name

    print(f"Best candidate is {best_candidate} with total {max_points} points.\nRanking:")

    users_info = dict(sorted(users_info.items(), key=lambda x: x[0]))

    for username, values in users_info.items():
        print(username)
        values = dict(sorted(values.items(), key=lambda x: -x[1]))
        for con, po in values.items():
            print(f"#  {con} -> {po}")


sequence = input()
ranking(sequence)