def social_distribution(popul, border):
    for i in range(len(popul)):
        max_wage = max(popul)
        if popul[i] < border:
            index_max_wage = popul.index(max_wage)
            popul[index_max_wage] -= border - popul[i]
            popul[i] += border - popul[i]
    if [i for i in popul if i < border]:
        print("No equal distribution possible")
    else:
        print(popul)


population = list(map(int, input().split(", ")))
border_min_wage = int(input())

social_distribution(population, border_min_wage)