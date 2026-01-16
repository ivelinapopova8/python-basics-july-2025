year_tax = int(input())

shoes = 0.6* year_tax
equip = 0.8 * shoes
ball = equip/4
acssesoaries = ball/5
sum = year_tax + shoes+equip + ball + acssesoaries

print(f"{sum:.2f}")