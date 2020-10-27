
# Game of Blackjack
# Deal the user two random cards and show their values (assume Ace = 11)

cards = {
    'Two of Clubs': 2,
    'Three of Clubs': 3,
    'Four of Clubs': 4,
    'Five of Clubs': 5,
    'Six of Clubs': 6,
    'Seven of Clubs': 7,
    'Eight of Clubs': 8,
    'Nine of Clubs': 9,
    'Ten of Clubs': 10,
    'Jack of Clubs': 10,
    'Queen of Clubs': 10,
    'King of Clubs': 10,
    'Ace of Clubs': 11,

    'Two of Spades': 2,
    'Three of Spades': 3,
    'Four of Spades': 4,
    'Five of Spades': 5,
    'Six of Spades': 6,
    'Seven of Spades': 7,
    'Eight of Spades': 8,
    'Nine of Spades': 9,
    'Ten of Spades': 10,
    'Jack of Spades': 10,
    'Queen of Spades': 10,
    'King of Spades': 10,
    'Ace of Spades': 11,

    'Two of Hearts': 2,
    'Three of Hearts': 3,
    'Four of Hearts': 4,
    'Five of Hearts': 5,
    'Six of Hearts': 6,
    'Seven of Hearts': 7,
    'Eight of Hearts': 8,
    'Nine of Hearts': 9,
    'Ten of Hearts': 10,
    'Jack of Hearts': 10,
    'Queen of Hearts': 10,
    'King of Hearts': 10,
    'Ace of Hearts': 11,

    'Two of Diamonds': 2,
    'Three of Diamonds': 3,
    'Four of Diamonds': 4,
    'Five of Diamonds': 5,
    'Six of Diamonds': 6,
    'Seven of Diamonds': 7,
    'Eight of Diamonds': 8,
    'Nine of Diamonds': 9,
    'Ten of Diamonds': 10,
    'Jack of Diamonds': 10,
    'Queen of Diamonds': 10,
    'King of Diamonds': 10,
    'Ace of Diamonds': 11,
}

import random
deck = list(cards.keys())
random.shuffle(deck)

# players initial cards
card_one = cards[deck.pop()]
card_two = cards[deck.pop()]

hand_total = card_one + card_two
print(f"player: {hand_total}")

# dealers initial cards
card_one = cards[deck.pop()]
card_two = cards[deck.pop()]

dealer_total = card_one + card_two
print(f"dealer: {dealer_total}")

hand_over = False
while not hand_over:
    if hand_total == 21:
        print("Blackjack!")
        hand_over = True
    elif hand_total > 21:
        print("Bust!")
        hand_over = True
    else:
        another_card = input("Would you like another card (Y/N)? ")
        if another_card == "Y":
            hand_total += cards[deck.pop()]
        else:
            hand_over = True
        print(f"Player hand: {hand_total}")

# dealer's decisions
hand_over = False
while not hand_over:
    if dealer_total >= 17:
        hand_over = True
    else:
        dealer_total += cards[deck.pop()]

print(f"Dealer hand: {dealer_total}")

if hand_total > dealer_total and dealer_total <= 21 and hand_total <= 21 \
    or hand_total == 21 and dealer_total != 21 \
    or hand_total <= 21 and dealer_total > 21:
    print("You WIN!")
else:
    print("You LOSE!")
