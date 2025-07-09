# import random 
# coin = random.choice(["heads" , "tails"])

"""from random import choice     # helps to call the choice function directly

coin = choice(["heads" , "tails"])    # 50-50 chance of printing "heads" or "tails"
print(coin)"""

import random

"""number = random.randint(1, 10) # will print a random number between 1 to 10.
print(number)"""

cards = ["jack", "queen", "king"]
random.shuffle(cards) # will shuffle the cards in the list.
for card in cards:
    print(card)