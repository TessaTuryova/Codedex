# 17. Guess Number

tries = 0

guess = 0

while guess != 6 and tries < 5:
    guess = int(input('Guess the number: '))
    tries = tries + 1  # tries += 1 doesn't work hmm

if guess != 6:
    print('You ran out of tries.')
else:
    print('You got it!')

# The and operator returns True if both of the conditions are True. And returns False otherwise.
# The or operator returns True if at least one of the conditions is True. And returns False otherwise.
# The not operator returns True the condition is False. And reverse.

"""
example code:
if hunger > 4 and anger > 1:
    print("Hangry")

if coffee > 0 or bubble_tea > 0:
    print("☺️")

if not tired:
    print("Let's code!")
"""
