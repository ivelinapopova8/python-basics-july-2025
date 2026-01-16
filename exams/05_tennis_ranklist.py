from math import floor

WINNER_POINTS = 2000
FINAL_POINTS = 1200
SEMI_POINTS = 720

num_tournaments = int(input())
start_points = int(input())
win_torn = 0
points = 0

for tournament in range(num_tournaments):
    level = str(input())

    if level == "W":
        points += WINNER_POINTS
        win_torn += 1
    elif level == "F":
        points += FINAL_POINTS
    elif level == "SF":
        points += SEMI_POINTS

avg_points = points / num_tournaments
perc_win = (win_torn / num_tournaments) * 100

print(f"Final points: {points + start_points}")
print(f"Average points: {floor(avg_points)}")
print(f"{perc_win:.2f}%")