# 11. Coin Flip

import random

num = random.randint(0, 1)   # RNGesus will give us a random number that is either 0 or 1

if num > 0.5:
    print('Heads')
else:
    print('Tails')

# it went heads 3 times from 5 tries
