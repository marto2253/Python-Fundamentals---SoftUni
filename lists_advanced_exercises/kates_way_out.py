def way_out(rows):
    for i in range(rows):
        maze_input = input().split()
        for x in range(len(maze_input)):
            if maze_input[x] == " ":
                print(x)


rows = int(input())
way_out(rows)