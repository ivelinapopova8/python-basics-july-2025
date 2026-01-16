PRICE_STUDIO_MAY_OCTOBER = 50
PRICE_APARTMENT_MAY_OCTOBER = 65
PRICE_STUDIO_JUNE_SEPTEMBER = 75.20
PRICE_APARTMENT_JUNE_SEPTEMBER = 68.70
PRICE_STUDIO_JULY_AUGUST = 76
PRICE_APARTMENT_JULY_AUGUST = 77

STUDIO_DISCOUNT_7NIGHTS_MAY_OCTOBER = 0.05
STUDIO_DISCOUNT_14NIGHTS_MAY_OCTOBER = 0.30
STUDIO_DISCOUNT_14NIGHTS_JUNE_SEPTEMBER = 0.20
APARTMENT_DISCOUNT_14NIGHTS = 0.10

month = input()
nights = int(input())

sum_studio = 0
sum_apartment = 0

if (month == "May") or (month == "October"):
    sum_studio = nights * PRICE_STUDIO_MAY_OCTOBER
    sum_apartment = nights * PRICE_APARTMENT_MAY_OCTOBER
    if 14 >= nights > 7:
        sum_studio -= sum_studio * STUDIO_DISCOUNT_7NIGHTS_MAY_OCTOBER
    elif nights > 14:
        sum_studio -= sum_studio * STUDIO_DISCOUNT_14NIGHTS_MAY_OCTOBER
        sum_apartment -= sum_apartment * APARTMENT_DISCOUNT_14NIGHTS
elif (month == "June") or (month == "September"):
    sum_studio = nights * PRICE_STUDIO_JUNE_SEPTEMBER
    sum_apartment = nights * PRICE_APARTMENT_JUNE_SEPTEMBER
    if nights > 14:
        sum_studio -= sum_studio * STUDIO_DISCOUNT_14NIGHTS_JUNE_SEPTEMBER
        sum_apartment -= sum_apartment * APARTMENT_DISCOUNT_14NIGHTS
elif (month == "July") or (month == "August"):
    sum_studio = nights * PRICE_STUDIO_JULY_AUGUST
    sum_apartment = nights * PRICE_APARTMENT_JULY_AUGUST
    if nights > 14:
        sum_apartment -= sum_apartment * APARTMENT_DISCOUNT_14NIGHTS

print(f"Apartment: {sum_apartment:.2f} lv.")
print(f"Studio: {sum_studio:.2f} lv.")