PRICE_PUZZLE = 2.60
PRICE_DOLL = 3
PRICE_BEAR = 4.10
PRICE_MINION = 8.20
PRICE_TRUCK = 2

price_holiday = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_toys = puzzles + dolls + bears + minions + trucks
total_sum = ((puzzles * PRICE_PUZZLE) +
             (dolls * PRICE_DOLL) +
             (bears * PRICE_BEAR) +
             (minions * PRICE_MINION) +
             (trucks * PRICE_TRUCK))

if total_toys >= 50:
    total_sum -= total_sum * 0.25

total_sum -= total_sum * 0.10

if total_sum >= price_holiday:
    print(f"Yes! {total_sum - price_holiday:.2f} lv left.")
else:
    print(f"Not enough money! {price_holiday - total_sum:.2f} lv needed.")