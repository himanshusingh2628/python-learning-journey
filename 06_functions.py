# Python Functions

def greet(name):
    print("Hello,", name)


def add_numbers(a, b):
    return a + b


name = input("Enter your name: ")
greet(name)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)

print("Sum:", result)
