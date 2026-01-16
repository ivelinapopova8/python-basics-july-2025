from math import floor

biscuits =  0
dog_food = 0
cat_food = 0

days = int(input())
all_food = float(input())

for day in range(1, days + 1):
    dog = int(input())
    cat = int(input())

    if day % 3 == 0:
        biscuits += 0.1 * (dog + cat)

    dog_food += dog
    cat_food += cat

eaten_food = dog_food + cat_food
perc_food = eaten_food / all_food * 100
perc_dog = dog_food / eaten_food * 100
perc_cat = cat_food / eaten_food * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{perc_food:.2f}% of the food has been eaten.")
print(f"{perc_dog:.2f}% eaten from the dog.")
print(f"{perc_cat:.2f}% eaten from the cat.")

