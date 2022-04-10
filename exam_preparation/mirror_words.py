import re


def mirror_words(seq):

    pattern = r'(\#|\@)(?P<first_word>[A-Za-z]{3,})(\1){2}(?P<second_word>[A-Za-z]{3,})(\1)'

    regex = re.finditer(pattern, seq)

    counter = 0

    # mirror_matches = {}
    mirror_matches_list = []
    for match in regex:
        counter += 1
        if match.group('first_word') == match.group('second_word')[::-1]:
            # mirror_matches[match.group('first_word')] = match.group('second_word')
            mirror_matches_list.append(match.group('first_word')+' <=> '+match.group('second_word'))


    if counter == 0:
        print('No word pairs found!')
        print('No mirror words!')
    elif counter > 0 and len(mirror_matches_list) == 0:
        print(f'{counter} word pairs found!')
        print('No mirror words!')
    else:
        print(f'{counter} word pairs found!')
        print('The mirror words are:')
        # for k, v in mirror_matches.items():
        #     print(f'{k} <=> {v}')
        print(', '.join(mirror_matches_list))


sequence = input()
mirror_words(sequence)
