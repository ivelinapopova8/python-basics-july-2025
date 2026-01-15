PRICE_NAYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNER = 5
PRICE_BAGS = 0.40

naylon = int(input())
paint = int(input())
thinner = int(input())
hours_work = int(input())

naylon += 2
paint += (paint * 0.1)

sum_materials = ((naylon * PRICE_NAYLON) +
                 (paint * PRICE_PAINT) +
                 (thinner * PRICE_THINNER) + PRICE_BAGS)
sum_workers = (sum_materials * 0.30) * hours_work
total_sum = sum_materials + sum_workers

print(total_sum)