#Project2:Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.You decide to host your application on servers running in the cloud. You pick a hosting provider that charges $0.51 per hour. You will launch your service using one server and want to know how much it will cost to operate per day,per week, per month.Write a Python program that displays the answers to the following questions:

cost_per_hour = 0.51

cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

budget = 918
days_with_budget = budget / cost_per_day

print("Cost to operate one server:")
print("Per Day  : $", round(cost_per_day, 2))
print("Per Week : $", round(cost_per_week, 2))
print("Per Month: $", round(cost_per_month, 2))
print("With $918, you can operate one server for", int(days_with_budget), "days.")
