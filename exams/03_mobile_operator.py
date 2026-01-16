SMALL_ONE = 9.98
MIDDLE_ONE = 18.99
LARGE_ONE = 25.98
EXTRALARGE_ONE = 35.99
SMALL_TWO = 8.58
MIDDLE_TWO = 17.09
LARGE_TWO = 23.59
EXTRALARGE_TWO = 31.79

PLUS_10 = 5.5
PLUS_30 = 4.35
PLUS_MORE = 3.85
DISCOUNT_2 = 0.0375

years = input()
type = input()
internet = input()
months = int(input())
money = 0

if years == "one":
    if type == "Small":
        money += SMALL_ONE * months
    elif type == "Middle":
        money += MIDDLE_ONE * months
    elif type == "Large":
        money += LARGE_ONE * months
    elif type == "ExtraLarge":
        money += EXTRALARGE_ONE * months
    if internet == "yes":
        if type == "Small":
            money += PLUS_10 * months
        elif (type == "Middle") or (type == "Large"):
            money += PLUS_30 * months
        elif type == "ExtraLarge":
            money += PLUS_MORE * months
elif years == "two":
    if type == "Small":
        money += SMALL_TWO * months
    elif type == "Middle":
        money += MIDDLE_TWO * months
    elif type == "Large":
        money += LARGE_TWO * months
    elif type == "ExtraLarge":
        money += EXTRALARGE_TWO * months
    if internet == "yes":
        if type == "Small":
            money += PLUS_10 * months
        elif (type == "Middle") or (type == "Large"):
            money += PLUS_30 * months
        elif type == "ExtraLarge":
            money += PLUS_MORE * months
    money -= money * DISCOUNT_2

print(f"{money:.2f} lv.")

