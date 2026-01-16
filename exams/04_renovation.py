from math import ceil

height = int(input())
weight = int(input())
perc_not = int(input()) / 100

area = height * weight * 4
area -= area * perc_not
area = ceil(area)

painted = 0

while True:
    command = input()
    if command == "Tired!":
        print(f"{area - painted} quadratic m left.")
        break

    liters = int(command)

    painted += liters

    if painted > area:
        print(f"All walls are painted and you have {painted - area} l paint left!")
        break
    elif painted == area:
        print(f"All walls are painted! Great job, Pesho!")
        break

