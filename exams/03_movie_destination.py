WINTER_DUBAI = 45_000
WINTER_SOFIA = 17_000
WINTER_LONDON = 24_000
SUMMER_DUBAI = 40_000
SUMMER_SOFIA = 12_500
SUMMER_LONDON = 20_250

DISCOUNT_DUBAI = 0.3
PLUS_SOFIA = 0.25

budget = float(input())
destiny = input()
season = input()
days = int(input())

total_sum = 0

if season == "Winter":
    if destiny == "Dubai":
        total_sum += WINTER_DUBAI * days
    elif destiny == "Sofia":
        total_sum += WINTER_SOFIA * days
    elif destiny == "London":
        total_sum += WINTER_LONDON * days
elif season == "Summer":
    if destiny == "Dubai":
        total_sum += SUMMER_DUBAI * days
    elif destiny == "Sofia":
        total_sum += SUMMER_SOFIA * days
    elif destiny == "London":
        total_sum += SUMMER_LONDON * days

if destiny == "Dubai":
    total_sum -= total_sum * DISCOUNT_DUBAI
elif destiny == "Sofia":
    total_sum += total_sum * PLUS_SOFIA

if budget >= total_sum:
    print(f"The budget for the movie is enough! We have {budget - total_sum:.2f} leva left!")
else:
    print(f"The director needs {total_sum - budget:.2f} leva more!")