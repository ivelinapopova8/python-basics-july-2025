NEED_POINTS = 1250.5

actor_name = input()
academy_points = float(input())
jury = int(input())
nominated = False

for _ in range(jury):
    name_jury = input()
    points = float(input())

    academy_points += (len(name_jury) * points / 2)

    if academy_points > NEED_POINTS:
        nominated = True
        break

if nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {NEED_POINTS - academy_points:.1f} more!")