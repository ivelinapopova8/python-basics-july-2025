budget = float(input())
num_series = int(input())

money = 0

for _ in range(num_series):
    name = input()
    price = float(input())

    if name == "Thrones":
        money += price * 0.5
    elif name == "Lucifer":
        money += price * 0.6
    elif name == "Protector":
        money += price * 0.7
    elif name == "TotalDrama":
        money += price * 0.8
    elif name == "Area":
        money += price * 0.9
    else:
        money += price

if budget >= money:
    print(f"You bought all the series and left with {budget - money:.2f} lv.")
else:
    print(f"You need {money - budget:.2f} lv. more to buy the series!")