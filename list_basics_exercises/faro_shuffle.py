card_deck = input()
shuffles = int(input())
shuffled_deck = card_deck.split(" ")
for i in range(shuffles):
    deck_1 = shuffled_deck[:len(shuffled_deck) // 2]
    deck_2 = shuffled_deck[len(shuffled_deck) // 2:]
    shuffled_deck = [cards for cards in zip(deck_1, deck_2) for cards in cards]
print(shuffled_deck)