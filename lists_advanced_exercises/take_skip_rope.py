def take_skip_rope(text):
    number_list = [int(i) for i in text if i.isnumeric()]
    non_number_list = [i for i in text if not i.isnumeric()]

    take_list = [int(number_list[i]) for i in range(len(number_list)) if i % 2 == 0]
    skip_list = [int(number_list[i]) for i in range(len(number_list)) if i % 2 != 0]

    result = ""
    skipped_chars = 0

    for i, x in zip(take_list, skip_list):
        index_i = i
        index_x = x
        skipped_chars += index_x
        result += ''.join(non_number_list[:index_i])

        del non_number_list[0:index_i + index_x]

    print(result)


text_input = input()
take_skip_rope(text_input)
