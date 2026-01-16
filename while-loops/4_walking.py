GOAL_STREPS = 10_000

count_steps = 0

while count_steps < GOAL_STREPS:
    steps = input()

    if steps == "Going home":
        steps_home = int(input())
        count_steps += steps_home
        break

    count_steps += int(steps)

if count_steps >= GOAL_STREPS:
    print("Goal reached! Good job!")
    print(f"{count_steps - GOAL_STREPS} steps over the goal!")
else:
    print(f"{GOAL_STREPS - count_steps} more steps to reach goal.")