# 16. Enter PIN

print("BANK OF CODEDEX")

pin = int(input("Enter your PIN: "))

while pin != 1234:
    pin = int(input("Incorrect PIN. Try again: "))

    if pin == 1234:
        print("PIN accepted.")
