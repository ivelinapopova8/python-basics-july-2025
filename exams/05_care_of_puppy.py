buy_food = int(input()) * 1000
need_food = 0

while True:
    grams = input()

    if grams == "Adopted":
        break

    need_food += int(grams)

if need_food <= buy_food:
    print(f"Food is enough! Leftovers: {buy_food - need_food} grams.")
else:
    print(f"Food is not enough. You need {need_food - buy_food} grams more.")