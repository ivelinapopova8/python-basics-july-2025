border_first = int(input())
border_second = int(input())
border_third = int(input())

for num_1 in range(1, border_first + 1):
    if num_1 % 2 != 0:
        continue

    for num_2 in range(1, border_second + 1):
        if num_2 not in [2, 3, 5, 7]:
            continue

        for num_3 in range(1, border_third + 1):
            if num_3 % 2 != 0:
                continue

            print(num_1, num_2, num_3)


