best_player_goals = -1
best_player = ""
is_hetric = False

while True:
    name = input()
    if name == "END":
        break

    goals = int(input())

    if goals > best_player_goals:
        best_player = name
        best_player_goals = goals

    if goals >= 3:
        is_hetric = True
    else:
        is_hetric = False

    if goals >= 10:
        break

print(f"{best_player} is the best player!")
if is_hetric:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")