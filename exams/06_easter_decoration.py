DISCOUNT_EVEN = 0.2
PRICE_BASKET = 1.5
PRICE_WREATH = 3.80
PRICE_CHOCOLATE_BUNNY = 7

all_sum = 0
clients = int(input())

for _ in range(clients):
    num_things = 0
    price = 0

    while True:
        thing = input()

        if thing == "Finish":
            break

        num_things += 1
        if thing == "basket":
            price += PRICE_BASKET
        elif thing == "wreath":
            price += PRICE_WREATH
        elif thing == "chocolate bunny":
            price += PRICE_CHOCOLATE_BUNNY

    if num_things % 2 == 0:
        price -= price * DISCOUNT_EVEN
    all_sum += price
    print(f"You purchased {num_things} items for {price:.2f} leva.")

print(f"Average bill per client is: {all_sum/clients:.2f} leva.")