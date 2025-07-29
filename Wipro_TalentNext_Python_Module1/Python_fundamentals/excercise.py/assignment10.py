#Write a program to find if the given number is a palindrome or not using a while loop.

num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print(original, "is a palindrome.")
else:
    print(original, "is not a palindrome.")
