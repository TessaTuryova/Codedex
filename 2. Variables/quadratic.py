# 9. Quadratic

# input -> default is string
username = input("Enter your name: ")
print(username)

# input for int
age = int(input("Enter your age: "))  # only integer is accepted, else error is displayed
print(age)

# task
print("Quadratic formula calculator")
a = int(input("Enter value for a (int): "))
b = int(input("Enter value for b (int): "))
c = int(input("Enter value for c (int): "))

root1 = (-b + ((b ** 2 - (4 * a * c)) ** 0.5)) / 2 * a
root2 = (-b - ((b ** 2 - (4 * a * c)) ** 0.5)) / 2 * a
print(root1)
print(root2)
