PRICE_KOZUNAK = 3.20
PRICE_EGGS = 4.35
PRICE_COOKIES = 5.40
PRICE_PAINT = 0.15

num_kozunaci = int(input())
num_kori_eggs = int(input())
num_cookies = int(input())
eggs = num_kori_eggs * 12

sum_all = ((PRICE_KOZUNAK * num_kozunaci) +
           (PRICE_EGGS * num_kori_eggs) +
           (PRICE_COOKIES * num_cookies) +
           (PRICE_PAINT * eggs))
print(f"{sum_all:.2f}")