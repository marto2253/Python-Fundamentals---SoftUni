users = {"Tanya": {"fundamentals": 250, "oop": 350}, "Nikola": {"c#": 150, "python": 950}}

a = ['Mid', 'Support', 'Tank']
b = ['Tank']
# print(['yes' for i in a if i in b])

for i in a:
    if i in b:
        print(i)

