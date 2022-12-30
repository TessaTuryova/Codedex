# 14. Magic 8 Ball

import random

num = random.randint(0, 8) # generates rundom num from 0 to 8
print(num)

print("Question: Am I old?")

if num == 0:
    print("Yes - definitely.")
elif num == 1:
    print("It is decidedly so.")
elif num == 2:
    print("Without a doubt.")
elif num == 3:
    print("Reply hazy, try again.")
elif num == 4:
    print("Ask again later.")
elif num == 5:
    print("Better not tell you now.")
elif num == 6:
    print("My sources say no.")
elif num == 7:
    print("Outlook not so good.")
else:
    print("Very doubtful.")