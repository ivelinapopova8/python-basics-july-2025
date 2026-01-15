price_per_year = int(input())

PRICE_PER_SHOES = 0.60 * price_per_year
PRICE_PER_EQUIP = 0.80 * PRICE_PER_SHOES
PRICE_PER_BALL = 0.25 * PRICE_PER_EQUIP
PRICE_PER_ACCESSORIES = 0.20 * PRICE_PER_BALL

total_sum = price_per_year + PRICE_PER_SHOES + PRICE_PER_EQUIP + PRICE_PER_BALL + PRICE_PER_ACCESSORIES

print(total_sum)