import sys

num_films = int(input())
name_max = ""
name_min = ""
max_points = -sys.maxsize
min_points = sys.maxsize
all_points = 0

for film in range(num_films):
    name = input()
    points = float(input())
    all_points += points

    if points > max_points:
        max_points = points
        name_max = name

    if points < min_points:
        min_points = points
        name_min = name

avg_rating = all_points / num_films
print(f"{name_max} is with highest rating: {max_points:.1f}")
print(f"{name_min} is with lowest rating: {min_points:.1f}")
print(f"Average rating: {avg_rating:.1f}")