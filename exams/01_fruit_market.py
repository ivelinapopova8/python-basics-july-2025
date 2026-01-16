price_strawberries = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

price_raspberries = price_strawberries / 2
price_oranges = 0.6 * price_raspberries
price_bananas = 0.2 * price_raspberries

money = (price_strawberries * strawberries_kg) + (price_oranges * oranges_kg) + (price_bananas * bananas_kg) + (price_raspberries * raspberries_kg)

print(f"{money:.2f}")