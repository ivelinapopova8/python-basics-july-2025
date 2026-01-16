budget = float(input())
num_statists = int(input())
price_clothes = float(input())

decor = 0.1 * budget
DISCOUNT_150 = 0.1
sum_clothes = 0

if num_statists > 150:
    price_clothes = price_clothes - (price_clothes * DISCOUNT_150)
    sum_clothes = num_statists * price_clothes
else:
    sum_clothes = price_clothes * num_statists

sum_all = decor + sum_clothes
if budget >= sum_all:
    print(f"Action!")
    print(f"Wingard starts filming with {budget-sum_all:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {sum_all-budget:.2f} leva more.")