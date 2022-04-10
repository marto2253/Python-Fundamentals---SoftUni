to_do_notes = [int(i) for i in range(11)]
# to_do_notes = ["" for i in range(11)]

notes = input()

while notes != "End":
    split_notes = notes.split("-")
    importance = int(split_notes[0])
    task = split_notes[1]
    # noinspection PyTypeChecker
    to_do_notes[importance] = task

    notes = input()

# final_to_do_notes = [i for i in to_do_notes if i != ""]
final_to_do_notes = [i for i in to_do_notes if type(i) != int]

print(final_to_do_notes)