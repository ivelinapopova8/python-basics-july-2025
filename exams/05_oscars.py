NEED_POINTS = 1250.5

name_actor = input()
academy_points = float(input())
num_jury = int(input())
is_select = False

for _ in range(num_jury):
    jury_name = input()
    given_points = float(input())

    academy_points += len(jury_name) * given_points / 2

    if academy_points >= NEED_POINTS:
        is_select = True
        break

if is_select:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {NEED_POINTS - academy_points:.1f} more!")