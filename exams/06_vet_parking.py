days = int(input())
hours_per_day = int(input())
money = 0

for day in range(1, days + 1):
    day_money = 0
    for hour in range(1, hours_per_day + 1):

        if (day % 2 == 0) and (hour % 2 != 0):
            day_money += 2.5
        elif (day % 2 != 0) and (hour % 2 == 0):
            day_money += 1.25
        else:
            day_money += 1

    money += day_money
    print(f"Day: {day} - {day_money:.2f} leva")

print(f"Total: {money:.2f} leva")
