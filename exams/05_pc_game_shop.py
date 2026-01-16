hearthstone = 0
fornite = 0
overwatch = 0
others = 0
total = 0

num = int(input())

for _ in range(num):
    game = input()

    if game == "Hearthstone":
        hearthstone += 1
        total += 1
    elif game == "Fornite":
        fornite += 1
        total += 1
    elif game == "Overwatch":
        overwatch += 1
        total += 1
    else:
        others += 1
        total += 1

print(f"Hearthstone - {hearthstone / total * 100:.2f}%")
print(f"Fornite - {fornite / total * 100:.2f}%")
print(f"Overwatch - {overwatch / total * 100:.2f}%")
print(f"Others - {others / total * 100:.2f}%")