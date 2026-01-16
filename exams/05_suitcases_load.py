capacity = float(input())
is_end = False
no_more = False
suitcases = 0

while True:
    command = input()

    if command == "End":
        is_end = True
        break

    volume = float(command)
    suitcases += 1

    if suitcases % 3 == 0:
        volume += 0.10 * volume

    if capacity < volume:
        no_more = True
        suitcases -= 1
        break

    capacity -= volume

if is_end:
    print(f"Congratulations! All suitcases are loaded!")
elif no_more:
    print(f"No more space!")

print(f"Statistic: {suitcases} suitcases loaded.")

