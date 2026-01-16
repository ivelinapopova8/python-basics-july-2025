price_floar = float(input())
kg_floar = float(input())
kg_sugar = float(input())
num_kori_eggs = int(input())
num_maq = int(input())

price_sugar = 0.75 * price_floar
price_kora_eggs = 1.10 * price_floar
price_maq = 0.2 * price_sugar

sum_all = ((price_floar * kg_floar) +
           (price_sugar * kg_sugar) +
           (price_kora_eggs * num_kori_eggs) +
           (price_maq * num_maq))
print(f"{sum_all:.2f}")