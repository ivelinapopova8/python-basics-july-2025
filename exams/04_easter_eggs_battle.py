eggs1 = int(input())
eggs2 = int(input())
is_end = False
is_one = False
is_two = False

while True:
    winner = input()
    if winner == "End":
        is_end = True
        break

    if winner == "one":
        eggs2 -= 1
    elif winner == "two":
        eggs1 -= 1

    if eggs1 == 0:
        is_two = True
        break

    if eggs2 == 0:
        is_one = True
        break

if is_end:
    print(f"Player one has {eggs1} eggs left.")
    print(f"Player two has {eggs2} eggs left.")
elif is_one:
    print(f"Player two is out of eggs. Player one has {eggs1} eggs left.")
elif is_two:
    print(f"Player one is out of eggs. Player two has {eggs2} eggs left.")