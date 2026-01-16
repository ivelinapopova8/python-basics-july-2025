ESPRESSO_NO_SUGAR = 0.90
ESPRESSO_NORMAL = 1
ESPRESSO_ADD_SUGAR = 1.20
CAPUCHINO_NO_SUGAR = 1
CAPUCHINO_NORMAL = 1.20
CAPUCHINO_ADD_SUGAR = 1.60
TEA_NO_SUGAR = 0.50
TEA_NORMAL = 0.60
TEA_ADD_SUGAR = 0.70

DISCOUNT_NO_SUGAR = 0.35
DISCOUNT_ESPRESSO_5 = 0.25
DISCOUNT_15 = 0.20

drink = input()
sugar = input()
num_drinks = int(input())
money = 0

if drink == "Espresso":
    if sugar == "Without":
        money += ESPRESSO_NO_SUGAR * num_drinks
    elif sugar == "Normal":
        money += ESPRESSO_NORMAL * num_drinks
    elif sugar == "Extra":
        money += ESPRESSO_ADD_SUGAR * num_drinks
elif drink == "Cappuccino":
    if sugar == "Without":
        money += CAPUCHINO_NO_SUGAR * num_drinks
    elif sugar == "Normal":
        money += CAPUCHINO_NORMAL * num_drinks
    elif sugar == "Extra":
        money += CAPUCHINO_ADD_SUGAR * num_drinks
elif drink == "Tea":
    if sugar == "Without":
        money += TEA_NO_SUGAR * num_drinks
    elif sugar == "Normal":
        money += TEA_NORMAL * num_drinks
    elif sugar == "Extra":
        money += TEA_ADD_SUGAR * num_drinks

if sugar == "Without":
    money -= money * DISCOUNT_NO_SUGAR

if (drink == "Espresso") and (num_drinks >= 5):
    money -= money * DISCOUNT_ESPRESSO_5

if money > 15:
    money -= money * DISCOUNT_15

print(f"You bought {num_drinks} cups of {drink} for {money:.2f} lv.")