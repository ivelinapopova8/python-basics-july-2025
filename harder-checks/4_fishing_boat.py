SPRING_PRICE = 3000
SUMMER_AUTUMN_PRICE = 4200
WINTER_PRICE = 2600

SMALL_GROUP_DISCOUNT = 0.10
MEDIUM_GROUP_DISCOUNT = 0.15
LARGE_GROUP_DISCOUNT = 0.25

budget = int(input())
season = input()
number_fishermans = int(input())

sum = 0

if season == "Spring":
    sum += SPRING_PRICE
    if number_fishermans <= 6:
        sum -= sum * SMALL_GROUP_DISCOUNT
    elif 7 <= number_fishermans <= 11:
        sum -= sum * MEDIUM_GROUP_DISCOUNT
    elif number_fishermans >= 12:
        sum -= sum * LARGE_GROUP_DISCOUNT
elif (season == "Summer") or (season == "Autumn"):
    sum += SUMMER_AUTUMN_PRICE
    if number_fishermans <= 6:
        sum -= sum * SMALL_GROUP_DISCOUNT
    elif 7 <= number_fishermans <= 11:
        sum -= sum * MEDIUM_GROUP_DISCOUNT
    elif number_fishermans >= 12:
        sum -= sum * LARGE_GROUP_DISCOUNT
elif season == "Winter":
    sum += WINTER_PRICE
    if number_fishermans <= 6:
        sum -= sum * SMALL_GROUP_DISCOUNT
    elif 7 <= number_fishermans <= 11:
        sum -= sum * MEDIUM_GROUP_DISCOUNT
    elif number_fishermans >= 12:
        sum -= sum * LARGE_GROUP_DISCOUNT

if (number_fishermans % 2 == 0) and (season != "Autumn" ):
    sum -= sum * 0.05

if budget >= sum:
    print(f"Yes! You have {budget - sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {sum - budget:.2f} leva.")