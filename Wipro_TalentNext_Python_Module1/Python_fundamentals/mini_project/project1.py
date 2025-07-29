#Project 1:Create a python program that asks the user how far they want to travel. If they want to travel less than three mlies tell them to ride Bicycle. If they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. If they want to travel three hundred miles or more tell them to driv

distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")
