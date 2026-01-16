num_1 = input()
num_2 = input()

num_1_1 = int(num_1[0])
num_1_2 = int(num_1[1])
num_1_3 = int(num_1[2])
num_1_4 = int(num_1[3])
num_2_1 = int(num_2[0])
num_2_2 = int(num_2[1])
num_2_3 = int(num_2[2])
num_2_4 = int(num_2[3])


for ch_1 in range(num_1_1, num_2_1 + 1):
    if ch_1 % 2 == 0:
        continue
    for ch_2 in range(num_1_2, num_2_2 + 1):
        if ch_2 % 2 == 0:
            continue
        for ch_3 in range(num_1_3, num_2_3 + 1):
            if ch_3 % 2 == 0:
                continue
            for ch_4 in range(num_1_4, num_2_4 + 1):
                    if ch_4 % 2 == 0:
                        continue
                    print(f"{ch_1}{ch_2}{ch_3}{ch_4}", end = " ")
