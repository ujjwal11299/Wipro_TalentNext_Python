#Write a progras to print prime numbers between 10 and 99.

for num in range(10, 100):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
