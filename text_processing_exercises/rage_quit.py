def rage_quit(seq):
    rage_message = ''
    current_chars = ''
    unique_chars = ''
    for i in seq:
        if i.isnumeric():
            rage_message += current_chars.upper() * int(i)
            current_chars = ''
        else:
            if i.lower() not in unique_chars:
                unique_chars += i.lower()
            current_chars += i

    return f'Unique symbols used: {len(unique_chars)}\n{rage_message}'


sequence = input()
print(rage_quit(sequence))
