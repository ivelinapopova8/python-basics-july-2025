

BG_SUMMER = 0.30
BG_WINTER = 0.70
BALKAN_SUMMER = 0.40
BALKAN_WINTER = 0.80
EUROPE_VACATION = 0.90

budget = float(input())
season = input()

destiny = ""
place = ""
sum = 0

if budget <= 100:
    destiny = "Bulgaria"
    if season == "summer":
        place = "Camp"
        sum += budget * BG_SUMMER
    elif season == "winter":
        place = "Hotel"
        sum += budget * BG_WINTER
elif 100 < budget <= 1000:
    destiny = "Balkans"
    if season == "summer":
        place = "Camp"
        sum += budget * BALKAN_SUMMER
    elif season == "winter":
        place = "Hotel"
        sum += budget * BALKAN_WINTER
elif budget > 1000:
    destiny = "Europe"
    sum += budget * EUROPE_VACATION
    place = "Hotel"


print(f"Somewhere in {destiny}")
print(f"{place} - {sum:.2f}")