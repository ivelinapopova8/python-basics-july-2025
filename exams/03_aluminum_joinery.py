num_joinery = int(input())
type = input()
pick_up = input()
money = 0
is_valid = True

if num_joinery < 10:
    print("Invalid order")
    is_valid = False

if type == "90X130":
    money += num_joinery * 110
    if num_joinery > 60:
        money -= money * 0.08
    elif num_joinery > 30:
        money -= money * 0.05
elif type == "100X150":
    money += num_joinery * 140
    if num_joinery > 80:
        money -= money * 0.1
    elif num_joinery > 40:
        money -= money * 0.06
elif type == "130X180":
    money += num_joinery * 190
    if num_joinery > 50:
        money -= money * 0.12
    elif num_joinery > 20:
        money -= money * 0.07
elif type == "200X300":
    money += num_joinery * 250
    if num_joinery > 50:
        money -= money * 0.14
    elif num_joinery > 25:
        money -= money * 0.09

if pick_up == "With delivery":
    money += 60

if num_joinery > 99:
    money -= money * 0.04

if is_valid:
    print(f"{money:.2f} BGN")