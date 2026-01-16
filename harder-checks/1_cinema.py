PRICE_PREMIERE = 12
PRICE_NORMAL = 7.50
PRICE_DISCOUNT = 5

projection = input()
rows = int(input())
columns = int(input())

capacity = rows * columns
sum = 0

if projection == "Premiere":
    sum = capacity * PRICE_PREMIERE
elif projection == "Normal":
    sum = capacity * PRICE_NORMAL
elif projection == "Discount":
    sum = capacity * PRICE_DISCOUNT

print(f"{sum:.2f} leva")