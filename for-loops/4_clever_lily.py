BROTHER_MONEY = 1

ages = int(input())
washing_machine = float(input())
price_toy = int(input())

birthday_money = 10
lily_money = 0
toys = 0

for age in range(1, ages + 1):
    if age % 2 == 0:
        lily_money += (birthday_money - BROTHER_MONEY)
        birthday_money += 10
    else:
        toys += 1

lily_money += toys * price_toy

if lily_money >= washing_machine:
    print(f"Yes! {lily_money - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - lily_money:.2f}")