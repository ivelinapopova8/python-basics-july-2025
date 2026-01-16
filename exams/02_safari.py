PRICE_1L_GAS = 2.1
PRICE_GUID = 100
DISCOUNT_SATURDAY = 0.1
DISCOUNT_SUNDAY = 0.2

budget = float(input())
liters_gas = float(input())
day = input()

money = PRICE_GUID + (liters_gas * PRICE_1L_GAS)

if day == "Saturday":
    money -= money * DISCOUNT_SATURDAY
elif day == "Sunday":
    money -= money * DISCOUNT_SUNDAY

if budget >= money:
    print(f"Safari time! Money left: {budget - money:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {money - budget:.2f} lv.")