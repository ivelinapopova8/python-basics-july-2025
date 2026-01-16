PRICE_DRINK_JOHN_WICK = 12
PRICE_POPS_JOHN_WICK = 15
PRICE_MENU_JOHN_WICK = 19
PRICE_DRINK_STAR_WARS = 18
PRICE_POPS_STAR_WARS = 25
PRICE_MENU_STAR_WARS = 30
PRICE_DRINK_JUMANJI = 9
PRICE_POPS_JUMANJI = 11
PRICE_MENU_JUMANJI = 14

DISCOUNT_SW_4 = 0.3
DISCOUNT_J_2 = 0.15

film = input()
product = input()
tickets = int(input())

total_sum = 0

if film == "John Wick":
    if product == "Drink":
        total_sum += PRICE_DRINK_JOHN_WICK * tickets
    elif product == "Popcorn":
        total_sum += PRICE_POPS_JOHN_WICK * tickets
    elif product == "Menu":
        total_sum += PRICE_MENU_JOHN_WICK * tickets
elif film == "Star Wars":
    if product == "Drink":
        total_sum += PRICE_DRINK_STAR_WARS * tickets
    elif product == "Popcorn":
        total_sum += PRICE_POPS_STAR_WARS * tickets
    elif product == "Menu":
        total_sum += PRICE_MENU_STAR_WARS * tickets

    if tickets >= 4:
        total_sum -= total_sum * DISCOUNT_SW_4
elif film == "Jumanji":
    if product == "Drink":
        total_sum += PRICE_DRINK_JUMANJI * tickets
    elif product == "Popcorn":
        total_sum += PRICE_POPS_JUMANJI * tickets
    elif product == "Menu":
        total_sum += PRICE_MENU_JUMANJI * tickets

    if tickets == 2:
        total_sum -= total_sum * DISCOUNT_J_2

print(f"Your bill is {total_sum:.2f} leva.")