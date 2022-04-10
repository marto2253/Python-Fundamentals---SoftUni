def counter_strike(t_e):
    win_counter = 0

    current_input = input()
    while current_input != "End of battle":
        int_ci = int(current_input)
        if t_e - int_ci >= 0:
            t_e -= int_ci
            win_counter += 1
            if win_counter % 3 == 0:
                t_e += win_counter
        else:
            return f"Not enough energy! Game ends with {win_counter} won battles and {t_e} energy"
        current_input = input()
    return f"Won battles: {win_counter}. Energy left: {t_e}"


total_energy = int(input())
print(counter_strike(total_energy))
