days = int(input())
win_days = 0
lose_days = 0
money = 0

for _ in range(days):
    money_day = 0
    win_games = 0
    lose_games = 0
    while True:
        sport = input()

        if sport == "Finish":
            break

        result = input()

        if result == "win":
            win_games += 1
            money_day += 20
        elif result == "lose":
            lose_games += 1

    if win_games > lose_games:
        money_day += money_day * 0.1
        win_days += 1
    else:
        lose_days += 1

    money += money_day

if win_days > lose_days:
    money += money * 0.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")

