start_points = 301
name = str(input())
is_retired = False
is_0 = False
times = 0
not_times = 0

while True:
    pole = str(input())
    if pole == "Retire":
        is_retired = True
        break
    points = int(input())
    wins = 0

    if pole == "Single":
        wins = points
    elif pole == "Double":
        wins = points * 2
    elif pole == "Triple":
        wins = points * 3

    if start_points >= wins:
        start_points -= wins
        times += 1
    else:
        not_times += 1
        continue

    if start_points == 0:
        is_0 = True
        break

if is_0:
    print(f"{name} won the leg with {times} shots.")
elif is_retired:
    print(f"{name} retired after {not_times} unsuccessful shots.")
