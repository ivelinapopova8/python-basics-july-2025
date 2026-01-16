num_mens = int(input())
num_womens = int(input())
max_tables = int(input())
is_full = False

counter = 0

for men in range(1, num_mens + 1):
    for women in range(1, num_womens + 1):
        counter += 1
        print(f"({men} <-> {women})", end = " ")
        if max_tables == counter:
            is_full = True
            break
    if is_full:
        break