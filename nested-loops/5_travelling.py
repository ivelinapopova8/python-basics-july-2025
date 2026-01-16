while True:
    destination = input()
    if destination == "End":
        break

    budget = float(input())
    money = 0.0

    while money < budget:
        new_money = float(input())
        money += new_money

    print(f"Going to {destination}!")