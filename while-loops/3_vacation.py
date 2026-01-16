needed_money = float(input())
balance = float(input())

days = 0
spending_days = 0


while spending_days < 5 and balance < needed_money:
    activity = input()
    money = float(input())

    if activity == "spend":
        spending_days += 1
        if balance >= money:
            balance -= money
        else:
            balance = 0

    if activity == "save":
        balance += money
        spending_days = 0

    days += 1

if spending_days >= 5:
    print(f"You can't save the money.")
    print(f"{days}")
elif balance >= needed_money:
    print(f"You saved the money for {days} days.")