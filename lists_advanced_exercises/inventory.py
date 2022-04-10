journal = input().split(", ")

commands = input()

while commands != "Craft!":
    split_commands = commands.split(" - ")
    action = split_commands[0]
    if action == "Collect":
        item = split_commands[1]
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        item = split_commands[1]
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        items = str(split_commands[1]).split(":")
        if items[0] in journal:
            index = journal.index(items[0])
            journal.insert(index + 1, items[1])
    elif action == "Renew":
        item = split_commands[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)
    commands = input()

print(', '.join(journal))
