#Write a progrse to check if a given number is prime or not.

num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
