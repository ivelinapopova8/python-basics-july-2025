EURO = 1.94

price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

sum = ((price_vegetables * kg_vegetables) +
       (price_fruits * kg_fruits))

sum_euro = sum / EURO

print(f"{sum_euro:.2f}")