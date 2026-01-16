PRICE_ROSE = 5
PRICE_DAHLIA = 3.80
PRICE_TULIP = 2.80
PRICE_NARCISSUS = 3
PRICE_GLADIOLUS = 2.50

ROSES_DISCOUNT = 0.10
DAHLIAS_DISCOUNT = 0.15
TULIPS_DISCOUNT = 0.15
NARCISSUS_INCREASE = 0.15
GLADIOLUS_INCREASE = 0.20

flowers = input()
number = int(input())
budget = int(input())

sum = 0

if flowers == "Roses":
    sum = number * PRICE_ROSE
    if number > 80:
        sum -= (sum * ROSES_DISCOUNT)
elif flowers == "Dahlias":
    sum = number * PRICE_DAHLIA
    if number > 90:
        sum -= (sum * DAHLIAS_DISCOUNT)
elif flowers == "Tulips":
    sum = number * PRICE_TULIP
    if number > 80:
        sum -= (sum * TULIPS_DISCOUNT)
elif flowers == "Narcissus":
    sum = number * PRICE_NARCISSUS
    if number < 120:
        sum += (sum * NARCISSUS_INCREASE)
elif flowers == "Gladiolus":
    sum = number * PRICE_GLADIOLUS
    if number < 80:
        sum += (sum * GLADIOLUS_INCREASE)

if budget >= sum:
    print(f"Hey, you have a great garden with {number} {flowers} and {budget - sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum - budget:.2f} leva more.")