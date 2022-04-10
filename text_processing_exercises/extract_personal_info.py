def extract_personal_info(num):

    for i in range(num):
        text = input()
        # splitted_text = input().split()
        # for word in splitted_text:
        #     if word.startswith('@') and word.endswith('|'):
        #         name += word[1:-1]
        #     elif word.startswith('#') and word.endswith('*'):
        #         age += word[1:-1]
        name_start, name_end = text.find('@'), text.find('|')
        age_start, age_end = text.find('#'), text.find('*')

        name = text[name_start + 1:name_end]
        age = text[age_start + 1:age_end]

        print(f'{name} is {age} years old.')


iters = int(input())
extract_personal_info(iters)
