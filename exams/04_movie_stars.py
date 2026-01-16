budget = float(input())
need_money = 0
is_action = False

while True:
    name = input()

    if name == "ACTION":
        is_action = True
        break

    if len(name) > 15:
        money = budget * 0.2
    else:
        money = float(input())

    if money > budget:
            print(f"We need {abs(budget - money):.2f} leva for our actors.")
            break

    budget -= money

if is_action:
    print(f"We are left with {budget:.2f} leva.")