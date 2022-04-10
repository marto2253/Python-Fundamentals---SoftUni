def electron_distribution(num_e):
    shells = list()
    position_of_shell = 1
    while sum(shells) != num_e:
        filling = (2 * position_of_shell**2)
        if filling + sum(shells) > electrons:
            shells.append(num_e - sum(shells))
        else:
            shells.append(filling)
        position_of_shell += 1

    print(shells)


electrons = int(input())
electron_distribution(electrons)
