age = float(input())
gender = input()
title = ""

if gender == "f":
    if age >= 16:
        title = "Ms."
    elif age < 16:
        title = "Miss"
elif gender == "m":
    if age >= 16:
        title = "Mr."
    elif age < 16:
        title = "Master"

print(title)