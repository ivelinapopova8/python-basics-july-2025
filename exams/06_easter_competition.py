import sys

kozunaci = int(input())
max_points = -sys.maxsize
max_name = ""
is_stop = False

for _ in range(kozunaci):
    name = input()
    all_points = 0

    while True:
        points = input()
        if points == "Stop":
            is_stop = True
            break

        points = int(points)
        all_points += points

    print(f"{name} has {all_points} points.")
    if all_points > max_points:
        max_points = all_points
        max_name = name
        print(f"{max_name} is the new number 1!")

print(f"{max_name} won competition with {max_points} points!")


