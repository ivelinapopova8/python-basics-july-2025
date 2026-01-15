PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEGAN_MENU = 8.15

chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

sum_menus = ((chicken_menus * PRICE_CHICKEN_MENU) +
             (fish_menus * PRICE_FISH_MENU) +
             (vegan_menus * PRICE_VEGAN_MENU))
price_dessert = sum_menus * 0.20
delivery_tax = 2.50
total_sum = sum_menus + price_dessert + delivery_tax

print(total_sum)