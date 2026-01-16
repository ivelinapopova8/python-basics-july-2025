winer_name = ""
winer_points = -1

while True:
    name = input()

    if name == "Stop":
        break

    n = len(name)
    current_points = 0

    for i in range(n):
        letter = name[i]
        ascii_code = ord(letter)
        number = int(input())
        if number == ascii_code:
            current_points += 10
        else:
            current_points += 2

    if current_points >= winer_points:
        winer_name = name
        winer_points = current_points


print(f"The winner is {winer_name} with {winer_points} points!")