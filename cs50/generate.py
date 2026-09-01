# from random import choice

# coin = random.choice(["heads", "tails"])
# print(coin)

# import random

# number = random.randint(1, 10)
# print(f"Random number between 1 and 10: {number}")

import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
