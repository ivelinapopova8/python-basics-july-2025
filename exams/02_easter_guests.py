from math import ceil

PRICE_KOZUNAK = 4
PRICE_EGG = 0.45

guests = int(input())
budget = int(input())

num_kozunaci = ceil(guests / 3)
num_eggs = guests * 2
sum_all = (PRICE_KOZUNAK * num_kozunaci) + (PRICE_EGG * num_eggs)

if budget >= sum_all:
    print(f"Lyubo bought {num_kozunaci} Easter bread and {num_eggs} eggs.")
    print(f"He has {budget - sum_all:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {sum_all - budget:.2f} lv. more.")