money = float(input())
until_year = int(input())

need_money = 0
age = 18

for year in range(1800, until_year + 1):
    if year % 2 == 0:
        need_money += 12000
        age += 1
    else:
        need_money += 12000 + 50 * age
        age += 1

if need_money <= money:
    print(f"Yes! He will live a carefree life and will have {money - need_money:.2f} dollars left.")
else:
    print(f"He will need {need_money - money:.2f} dollars to survive.")