STAR_NORMAL = 7.50
STAR_LUXURY = 10.50
STAR_ULTRA = 13.50
BOHEMIA_NORMAL = 7.35
BOHEMIA_LUXURY = 9.45
BOHEMIA_ULTRA = 12.75
GREEN_NORMAL = 8.15
GREEN_LUXURY = 10.25
GREEN_ULTRA = 13.25
FAVOURITE_NORMAL = 8.75
FAVOURITE_LUXURY = 11.55
FAVOURITE_ULTRA = 13.95

film = input()
room = input()
tickets = int(input())
sum_all = 0

if film == "A Star Is Born":
    if room == "normal":
        sum_all = STAR_NORMAL * tickets
    elif room == "luxury":
        sum_all = STAR_LUXURY * tickets
    elif room == "ultra luxury":
        sum_all = STAR_ULTRA * tickets
elif film == "Bohemian Rhapsody":
    if room == "normal":
        sum_all = BOHEMIA_NORMAL * tickets
    elif room == "luxury":
        sum_all = BOHEMIA_LUXURY * tickets
    elif room == "ultra luxury":
        sum_all = BOHEMIA_ULTRA * tickets
elif film == "Green Book":
    if room == "normal":
        sum_all = GREEN_NORMAL * tickets
    elif room == "luxury":
        sum_all = GREEN_LUXURY * tickets
    elif room == "ultra luxury":
        sum_all = GREEN_ULTRA * tickets
elif film == "The Favourite":
    if room == "normal":
        sum_all = FAVOURITE_NORMAL * tickets
    elif room == "luxury":
        sum_all = FAVOURITE_LUXURY * tickets
    elif room == "ultra luxury":
        sum_all = FAVOURITE_ULTRA * tickets

print(f"{film} -> {sum_all:.2f} lv.")