# 10. Currency

# recap
# Data types: int, float, str, bool.
# Arithmetic operators: +, -, *, /.
# The % modulo finds the remainder.
# The ** exponentiation finds the exponent.
# The input() function is used to get user input.
# The int() function converts a value into an integer number.

# task
print("Calculator that sums yuan, yen and won into $.")
yuan = int(input("What do you have left in yuan? "))
yen = int(input("What do you have left in yen? "))
won = int(input("What do you have left in won? "))

# conversion rates on 29th December 2022
rateYuan = 0.14
rateYen = 0.0075
rateWon = 0.00079

dollar = yuan * rateYuan + yen * rateYen + won * rateWon
print(dollar)
