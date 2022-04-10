import re


def emoji_detector(seq):

    cool_threshold = 1
    emojis = []
    emoji_count = 0

    cool_expression = r'\d+'
    cool_threshold_numbers = re.findall(cool_expression, seq)

    for i in cool_threshold_numbers:
        for num in i:
            cool_threshold *= int(num)

    emoji_expression = r'(::|\*\*)[A-Z][a-z]{2,}(\1)'
    emoji_matches = re.finditer(emoji_expression, seq)

    for match in emoji_matches:
        total = 0
        emoji_count += 1
        for letter in match.group()[2:-2]:
            total += ord(letter)
        if total > cool_threshold:
            emojis.append(match.group())

    print(f"Cool threshold: {cool_threshold}")
    joined = '\n'.join(emojis)
    print(f"{emoji_count} emojis found in the text. The cool ones are:\n{joined}")


sequence = input()
emoji_detector(sequence)
