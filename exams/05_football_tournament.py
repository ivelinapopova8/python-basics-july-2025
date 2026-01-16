name = input()
num_matches = int(input())
wins = 0
draws = 0
loses = 0
total = 0
points = 0
not_played = False

if num_matches == 0:
    not_played = True
    print(f"{name} hasn't played any games during this season.")

for _ in range(num_matches):
    result = input()

    if result == "W":
        wins += 1
        total += 1
        points += 3
    elif result == "D":
        draws += 1
        total += 1
        points += 1
    elif result == "L":
        loses += 1
        total += 1
        points += 0

if not not_played:
    print(f"{name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {wins / total * 100:.2f}%")
