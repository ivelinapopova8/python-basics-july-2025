MEN_GYM = 42
MEN_BOX = 41
MEN_YOGA = 45
MEN_ZUMBA = 34
MEN_DANCE = 51
MEN_PILATES = 39
WOMAN_GYM = 35
WOMAN_BOX = 37
WOMAN_YOGA = 42
WOMAN_ZUMBA = 31
WOMAN_DANCE = 53
WOMAN_PILATES = 37

DISCOUNT_STUDENTS = 0.2

budget = float(input())
gender = input()
age = int(input())
sport = input()
money = 0

if gender == "m":
    if sport == "Gym":
        money += MEN_GYM
    elif sport == "Boxing":
        money += MEN_BOX
    elif sport == "Yoga":
        money += MEN_YOGA
    elif sport == "Zumba":
        money += MEN_ZUMBA
    elif sport == "Dances":
        money += MEN_DANCE
    elif sport == "Pilates":
        money += MEN_PILATES
elif gender == "f":
    if sport == "Gym":
        money += WOMAN_GYM
    elif sport == "Boxing":
        money += WOMAN_BOX
    elif sport == "Yoga":
        money += WOMAN_YOGA
    elif sport == "Zumba":
        money += WOMAN_ZUMBA
    elif sport == "Dances":
        money += WOMAN_DANCE
    elif sport == "Pilates":
        money += WOMAN_PILATES

if age <= 19:
    money -= money * DISCOUNT_STUDENTS

if budget >= money:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${money - budget:.2f} more.")