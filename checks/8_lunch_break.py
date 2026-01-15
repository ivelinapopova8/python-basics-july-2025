from math import ceil

name_movie = str(input())
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
rest_time = break_duration * 1/4
left_time = break_duration - (lunch_time + rest_time)

if left_time >= episode_duration:
    print(f"You have enough time to watch {name_movie} and left with {ceil(left_time - episode_duration)} minutes free time.")
elif left_time < episode_duration:
    print(f"You don't have enough time to watch {name_movie}, you need {ceil(episode_duration - left_time)} more minutes.")