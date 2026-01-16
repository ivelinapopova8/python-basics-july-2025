need_sum = int(input())
sum_all = 0
times = 0
people_cash = 0
people_card = 0
sum_cash = 0
sum_card = 0

while sum_all < need_sum:
    thing = input()

    if thing == "End":
        print(f"Failed to collect required money for charity.")
        break

    price = int(thing)
    times += 1

    if times % 2 != 0:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            people_cash += 1
            sum_all += price
            sum_cash += price
    elif times % 2 == 0:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            people_card += 1
            sum_all += price
            sum_card += price

if need_sum <= sum_all:
    avg_cash = sum_cash / people_cash
    avg_card = sum_card / people_card
    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")




