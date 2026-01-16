PRICE_ROOM_ONE_PERSON = 18
PRICE_APARTMENT = 25
PRICE_PRESIDENT_APARTMENT = 35

DISCOUNT_APARTMENT_9NIGHTS = 0.30
DISCOUNT_APARTMENT_10_15NIGHTS = 0.35
DISCOUNT_APARTMENT_16NIGHTS = 0.50
DISCOUNT_PRESIDENT_APARTMENT_9NIGHTS = 0.10
DISCOUNT_PRESIDENT_APARTMENT_10_15NIGHTS = 0.15
DISCOUNT_PRESIDENT_APARTMENT_16NIGHTS = 0.20

POSITIVE_INCREASE = 0.25
NEGATIVE_DISCOUNT = 0.10

days = int(input())
room = input()
review = input()

nights = days - 1
sum = 0

if room == "room for one person":
    sum = nights * PRICE_ROOM_ONE_PERSON
elif room == "apartment":
    sum = nights * PRICE_APARTMENT
    if nights < 10:
        sum -= sum * DISCOUNT_APARTMENT_9NIGHTS
    elif 10 <= nights <= 15:
        sum -= sum * DISCOUNT_APARTMENT_10_15NIGHTS
    elif nights > 15:
        sum -= sum * DISCOUNT_APARTMENT_16NIGHTS
elif room == "president apartment":
    sum = nights * PRICE_PRESIDENT_APARTMENT
    if nights < 10:
        sum -= sum * DISCOUNT_PRESIDENT_APARTMENT_9NIGHTS
    elif 10 <= nights <= 15:
        sum -= sum * DISCOUNT_PRESIDENT_APARTMENT_10_15NIGHTS
    elif nights > 15:
        sum -= sum * DISCOUNT_PRESIDENT_APARTMENT_16NIGHTS

if review == "positive":
    sum += POSITIVE_INCREASE * sum
elif review == "negative":
    sum -= NEGATIVE_DISCOUNT * sum

print(f"{sum:.2f}")