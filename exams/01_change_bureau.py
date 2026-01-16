bitcoins = int(input())
chines = float(input())
komisions = float(input()) / 100

DOLAR = 1.76
EURO = 1.95
BITCOIN = 1168
CHINES_DOLAR = 0.15

money_b = bitcoins * BITCOIN
money_c = chines * CHINES_DOLAR
money_c = money_c * DOLAR
money_leva = money_b + money_c
money_euro = money_leva / EURO
money = money_euro - (money_euro * komisions)

print(f"{money:.2f}")