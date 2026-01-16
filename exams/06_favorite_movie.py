
counter = 0
max_points = -9999999999
max_film = ""

while True:
    name = input()
    points = 0

    if name == "STOP":
        break

    counter += 1

    for ch in name:
        if ch.isupper():
            points += ord(ch) - len(name)
        elif ch.islower():
            points += ord(ch) - 2 * len(name)
        else:
            points += ord(ch)

    if points > max_points:
        max_points = points
        max_film = name

    if counter == 7:
        print(f"The limit is reached.")
        break

print(f"The best movie for you is {max_film} with {max_points} ASCII sum.")