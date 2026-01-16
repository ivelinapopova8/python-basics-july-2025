budget = float(input())
is_stop = False
not_enough = False
count = 0
buy = 0
spend_money = 0

while True:
    product = input()

    if product == "Stop":
        is_stop = True
        break

    count += 1
    price = float(input())

    if count == 3:
        price = price / 2
        count = 0

    if price > budget:
        not_enough = True
        break

    budget -= price
    buy += 1
    spend_money += price

if is_stop:
    print(f"You bought {buy} products for {spend_money:.2f} leva.")
elif not_enough:
    print(f"You don't have enough money!")
    print(f"You need {abs(budget - price):.2f} leva!")