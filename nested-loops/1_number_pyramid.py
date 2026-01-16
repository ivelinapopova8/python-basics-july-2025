number = int(input())
counter = 0
is_done = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        counter += 1
        print(str(counter) + " ", end="")

        if counter == number:
            is_done = True
            break

    if is_done:
        break
    print()
