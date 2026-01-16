name1 = str(input())
name2 = str(input())
points1 = 0
points2 = 0
winner = ""
is_war = False
points = 0
is_end = False

while True:
    card1 =str(input())
    if card1 == "End of game":
        is_end = True
        break
    else:
        card1 = int(card1)
    card2 =int(input())
    if card1 > card2:
        points1 += card1 - card2
    elif card2 > card1:
        points2 += card2 - card1
    elif card1 == card2:
        is_war = True
        card11 = int(input())
        card22 = int(input())
        if card11 > card22:
            winner = name1
            points = points1
            break
        elif card22 > card11:
            winner = name2
            points = points2
            break

if is_war:
    print(f"Number wars!")
    print(f"{winner} is winner with {points} points")
elif is_end:
    print(f"{name1} has {points1} points")
    print(f"{name2} has {points2} points")