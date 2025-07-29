#Given two non-negative values,print true if they have the same last diigit

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % 10 == b % 10:
    print("true")
else:
    print("false")
