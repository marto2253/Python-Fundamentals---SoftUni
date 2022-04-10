employees = list(map(int, input().split(" ")))
factor = int(input())

happines = [i * factor for i in employees]
average = sum(happines) / len(happines)

happy_employees = [i for i in happines if i >= average]

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")