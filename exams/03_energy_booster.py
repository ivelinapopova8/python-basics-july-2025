SMALL_WATERMELON = 56 * 2
SMALL_MANGO = 36.66 * 2
SMALL_PINEAPPLE = 42.10 * 2
SMALL_RASPBERRY = 20 * 2
BIG_WATERMELON = 28.70 * 5
BIG_MANGO = 19.60 * 5
BIG_PINEAPPLE = 24.80 * 5
BIG_RASPBERRY = 15.20 * 5

DISCOUNT_400 = 0.15
DISCOUNT_1000 = 0.50

fruit = input()
size = input()
num = int(input())
money = 0

if size == "small":
    if fruit == "Watermelon":
        money += SMALL_WATERMELON * num
    elif fruit == "Mango":
        money += SMALL_MANGO * num
    elif fruit == "Pineapple":
        money += SMALL_PINEAPPLE * num
    elif fruit == "Raspberry":
        money += SMALL_RASPBERRY * num
elif size == "big":
    if fruit == "Watermelon":
        money += BIG_WATERMELON * num
    elif fruit == "Mango":
        money += BIG_MANGO * num
    elif fruit == "Pineapple":
        money += BIG_PINEAPPLE * num
    elif fruit == "Raspberry":
        money += BIG_RASPBERRY * num

if 400 <= money <= 1000:
    money -= money * DISCOUNT_400
elif money > 1000:
    money -= money * DISCOUNT_1000

print(f"{money:.2f} lv.")