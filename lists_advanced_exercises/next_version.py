version = list(map(int, input().split(".")))

if version[2] != 9:
    version[2] += 1
elif version[2] == 9 and version[1] != 9:
    version[1] += 1
    version[2] = 0
elif version[2] == 9 and version[1] == 9:
    version[0] += 1
    version[1] = 0
    version[2] = 0

print(f"{version[0]}.{version[1]}.{version[2]}")

