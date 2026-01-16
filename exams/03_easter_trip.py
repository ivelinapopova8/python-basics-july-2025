FRANCE_21_23 = 30
FRANCE_24_27 = 35
FRANCE_28_31 = 40
ITALY_21_23 = 28
ITALY_24_27 = 32
ITALY_28_31 = 39
GERMANY_21_23 = 32
GERMANY_24_27 = 37
GERMANY_28_31 = 43

destination = input()
dates = input()
nights = int(input())
price = 0

if destination == "France":
    if dates == "21-23":
        price = FRANCE_21_23 * nights
    elif dates == "24-27":
        price = FRANCE_24_27 * nights
    elif dates == "28-31":
        price = FRANCE_28_31 * nights
elif destination == "Italy":
    if dates == "21-23":
        price = ITALY_21_23 * nights
    elif dates == "24-27":
        price = ITALY_24_27 * nights
    elif dates == "28-31":
        price = ITALY_28_31 * nights
elif destination == "Germany":
    if dates == "21-23":
        price = GERMANY_21_23 * nights
    elif dates == "24-27":
        price = GERMANY_24_27 * nights
    elif dates == "28-31":
        price = GERMANY_28_31 * nights

print(f"Easter trip to {destination} : {price:.2f} leva.")