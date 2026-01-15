budget_movie = float(input())
statists = int(input())
statist_clothes = float(input())

decor = budget_movie * 0.10
clothes_price = statists * statist_clothes

if statists > 150:
    clothes_price -= clothes_price * 0.10

needed_money = clothes_price + decor

if needed_money > budget_movie:
    print("Not enough money!")
    print(f"Wingard needs {needed_money - budget_movie:.2f} leva more.")
elif needed_money <= budget_movie:
    print("Action!")
    print(f"Wingard starts filming with {budget_movie - needed_money:.2f} leva left.")