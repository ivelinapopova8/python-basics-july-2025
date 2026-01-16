DISCOUNT_7_NIGHTS = 0.05

budget = float(input())
nights = int(input())
price_night = float(input())
perc_taxes = int(input()) / 100

if nights > 7:
    price_night -= price_night * DISCOUNT_7_NIGHTS

money = nights * price_night
money += budget * perc_taxes

if budget >= money:
    print(f"Ivanovi will be left with {budget - money:.2f} leva after vacation.")
else:
    print(f"{money - budget:.2f} leva needed.")