def students(seq):
    courses = dict()

    while ":" in seq:
        info = seq.split(":")
        name = info[0]
        id = info[1]
        course = info[2]

        if course not in courses.keys():
            courses[course] = dict()

        courses[course][id] = name

        seq = input()

    seq = seq.replace("_", " ")

    # for keys, values in courses[seq].items():
    #     print(f"{values} - {keys}")
    #
    for i in courses[seq]:
        print(f"{courses[seq][i]} - {i}")

    # print('\n'.join({f'{courses[seq][i]} - {i}' for i in courses[seq]}))


sequence = input()
students(sequence)
