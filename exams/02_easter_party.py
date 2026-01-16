DISCOUNT_10_15 = 0.15
DISCOUNT_15_20 = 0.2
DISCOUNT_20 = 0.25

guests = int(input())
price_kuvert = float(input())
budget = float(input())
price_cake = 0.10 * budget

if 10 <= guests <= 15:
    price_kuvert -= price_kuvert * DISCOUNT_10_15
elif 15 < guests <= 20:
    price_kuvert -= price_kuvert * DISCOUNT_15_20
elif guests > 20:
    price_kuvert -= price_kuvert * DISCOUNT_20

sum_all = (guests * price_kuvert) + price_cake

if budget >= sum_all:
    print(f"It is party time! {budget - sum_all:.2f} leva left.")
else:
    print(f"No party! {sum_all - budget:.2f} leva needed.")