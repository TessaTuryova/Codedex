# 19. 99 Bottles

# String concatenation

for i in range(5):
    print('The square of ' + str(i) + ' is ' + str(i*i))

# HAVE TO ADD str() TO NOT TRIGGER ERROR FOR CODE ABOVE

print()

# String interpolation

for i in range(5):
    print(f'The square of {i} is {i*i}')

# Notice the f prefix before the quotes. This was introduced in the new Python 3.6 version.

# task

for i in range(99): # incomplete, goes from 99 to 1, missing last line
    print(f"{99 - i} bottles of beer on the wall")
    print(f"{99 - i} bottles of beer")
    print("Take one down, pass it around")

# alternatove

for i in range(99, 0, -1): # from 99 to 0, -1 by going once through loop
    print(f'{i} bottles of beer on the wall')
    print(f'{i} bottles of beer')
    print('take one down pass it around')
    print(f'{i-1} bottles of beer on the wall')