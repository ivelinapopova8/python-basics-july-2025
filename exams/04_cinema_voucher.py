vaucher = int(input())
tickets = 0
others = 0

while True:
    thing = input()

    if thing == "End":
        break

    if len(thing) > 8:
        price = ord(thing[0]) + ord(thing[1])
    else:
        price = ord(thing[0])

    if price > vaucher:
        break

    vaucher -= price

    if len(thing) > 8:
        tickets += 1
    else:
        others += 1

print(tickets)
print(others)