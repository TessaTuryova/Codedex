# 13. pH Levels

# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

grade = 0

if grade > 90:
    print('A')
elif grade > 80:
    print('B')
elif grade > 70:
    print('C')
elif grade > 60:
    print('D')
else:
    print('F')

#pH = 7
pH = int(input('Enter a pH level (0-14): '))

if pH > 7:
    print("Basic")
elif pH < 7:
    print("Acidic")
else:
    print("Neutral")