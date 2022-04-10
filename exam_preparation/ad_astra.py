import re


def ad_astra(seq):

    calories_day = 0

    expression = r'(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<exp_date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>[0-9]+)\1'

    calories_matches = re.finditer(expression, seq)
    matches = re.finditer(expression, seq)

    for m in calories_matches:
        if m:
            calories_day += int(m.group('calories'))

    print(f'You have food to last you for: {calories_day//2000} days!')

    for match in matches:
        if match:
            print(f"Item: {match.group('item')}, Best before: {match.group('exp_date')}, Nutrition: {match.group('calories')}")


sequence = input()
ad_astra(sequence)
