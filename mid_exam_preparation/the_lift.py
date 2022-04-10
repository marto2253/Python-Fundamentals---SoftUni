def lift(ppl, lift_s):
    max_size = 4
    for i in range(len(lift_s)):
        if int(lift_s[i]) == 0:
            if ppl - max_size >= 0:
                lift_s[i] += max_size
                ppl -= max_size
            else:
                lift_s[i] += ppl
                ppl -= ppl
        else:
            if ppl - max_size >= 0:
                ppl -= max_size - lift_s[i]
                lift_s[i] += max_size - lift_s[i]
            else:
                lift_s[i] += ppl
                ppl -= ppl
    if ppl == 0 and [int(i) for i in lift_s if i != 4]:
        print("The lift has empty spots!")
        print(' '.join([str(i) for i in lift_s]))
    elif ppl == 0 and [int(i) for i in lift_s if i == 4]:
        print(' '.join([str(i) for i in lift_s]))
    else:
        print(f"There isn't enough space! {ppl} people in a queue!")
        print(' '.join([str(i) for i in lift_s]))


people = int(input())
lift_space = [int(i) for i in input().split(" ")]
lift(people, lift_space)
