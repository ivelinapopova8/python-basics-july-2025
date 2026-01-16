wanted_height = int(input())
height = wanted_height - 30
all_jumps = 0

while True:
    tries = 3
    is_ok = False
    for _ in range(tries):
        jump = int(input())
        all_jumps += 1
        if jump > height:
            is_ok = True
            break
        else:
            continue
    if is_ok:
        if height >= wanted_height:
            print(f"Tihomir succeeded, he jumped over {height}cm after {all_jumps} jumps.")
            break
        else:
            height += 5
            continue
    else:
        print(f"Tihomir failed at {height}cm after {all_jumps} jumps.")
        break

