wanted_win = float(input())
money = 0

while True:
    coctail = input()

    if coctail == "Party!":
        print(f"We need {wanted_win - money:.2f} leva more.")
        break

    num = int(input())

    order = len(coctail) * num

    if order % 2 != 0:
        order -= order * 0.25

    money += order

    if money >= wanted_win:
        print(f"Target acquired.")
        break

print(f"Club income - {money:.2f} leva.")