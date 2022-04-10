def reception(r1, r2, r3, sc):
    students_per_hour = 0
    lunch_break = 0
    hours_needed = 0
    while True:
        lunch_break += 1
        if lunch_break % 4 == 0:
            hours_needed += 1
        if students_per_hour + r1 + r2 + r3 >= sc:
            hours_needed += 1
            break
        else:
            students_per_hour += r1 + r2 + r3
            hours_needed += 1

    return f"Time needed: {hours_needed}h."


reception1 = int(input())
reception2 = int(input())
reception3 = int(input())
students_count = int(input())

print(reception(reception1, reception2, reception3, students_count))
