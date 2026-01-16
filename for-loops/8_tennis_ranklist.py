from math import floor

POINTS_WINNER = 2000
POINTS_FINALIST = 1200
POINTS_SEMI = 720

tournaments = int(input())
points = int(input())
win_tour = 0
new_points = 0

for _ in range(tournaments):
    level = input()

    if level == "W":
        new_points += POINTS_WINNER
        win_tour += 1
    elif level == "F":
        new_points += POINTS_FINALIST
    elif level == "SF":
        new_points += POINTS_SEMI

avrg_points = new_points / tournaments
points += new_points

print(f"Final points: {points}")
print(f"Average points: {floor(avrg_points)}")
print(f"{win_tour / tournaments * 100 :.2f}%")
