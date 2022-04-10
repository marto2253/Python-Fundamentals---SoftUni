def numbers(s):
    average = sum(s) // len(s)
    counter = 0
    top_five = []
    while counter != 5:
        if max(s) > average:
            top_five.append(max(s))
            s.remove(max(s))
        else:
            break
        counter += 1

    if len(top_five) == 0:
        return "No"
    else:
        return ' '.join(str(i) for i in top_five)


sequence = list(map(int, input().split(" ")))
print(numbers(sequence))
