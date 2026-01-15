price_of_dog_food = 2.50
price_of_cat_food = 4
dog_packages = int(input())
cat_packages = int(input())
total_dog_food_price = price_of_dog_food*dog_packages
total_cat_food_price = price_of_cat_food*cat_packages
total_price = total_dog_food_price + total_cat_food_price
print(f"{total_price} lv.")