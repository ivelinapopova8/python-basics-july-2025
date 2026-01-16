from math import ceil

people = int(input())
tax_enter = float(input())
price_lounger = float(input())
price_umbrella = float(input())

money = people * tax_enter

people_lounger = ceil(people * 0.75)
money += people_lounger * price_lounger

people_umbrella = ceil(people / 2)
money += people_umbrella * price_umbrella

print(f"{money:.2f} lv.")