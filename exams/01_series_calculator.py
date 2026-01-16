from math import floor

name = input()
seasons = int(input())
episodes = int(input())
time_ep = float(input())

ep_ad = time_ep + time_ep * 0.2
total_time = (seasons * ep_ad * episodes) + (10 * seasons)

print(f"Total time needed to watch the {name} series is {floor(total_time)} minutes.")