# 14. Magic 8 Ball

import random

num = random.randint(0, 8)  # generates rundom num from 0 to 8
print(num)

question = input('Question: ')
# print("Question: Am I old?")

if num == 0:
    answer = "Yes - definitely."
elif num == 1:
    answer = "It is decidedly so."
elif num == 2:
    answer = "Without a doubt."
elif num == 3:
    answer = "Reply hazy, try again."
elif num == 4:
    answer = "Ask again later."
elif num == 5:
    answer = "Better not tell you now."
elif num == 6:
    answer = "My sources say no."
elif num == 7:
    answer = "Outlook not so good."
else:
    answer = "Very doubtful."

print('Question:      ' + question)
print('Magic 8 Ball:  ' + answer)