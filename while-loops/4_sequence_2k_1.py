num = int(input())
new_number = 0

while True:
    new_number = (2 * new_number) + 1

    if new_number > num:
        break
    print(new_number)