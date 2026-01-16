eggs = int(input())
sold = 0
is_close = False
is_notenough = False

while True:
    command = input()
    if command == "Close":
        is_close = True
        break

    num_eggs = int(input())

    if command == "Buy":
        if num_eggs > eggs:
            is_notenough = True
            break
        else:
            sold += num_eggs
            eggs -= num_eggs
    elif command == "Fill":
        eggs += num_eggs

if is_close:
    print(f"Store is closed!")
    print(f"{sold} eggs sold.")
elif is_notenough:
    print(f"Not enough eggs in store!")
    print(f"You can buy only {eggs}.")