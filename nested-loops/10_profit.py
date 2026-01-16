num_1 = int(input())
num_2 = int(input())
num_5 = int(input())
money = int(input())

for lv_1 in range(num_1 + 1):
    for lv_2 in range(num_2 + 1):
        for lv_5 in range(num_5 + 1):
            if lv_1 * 1 + lv_2 * 2 + lv_5 * 5 == money:
                print(f"{lv_1} * 1 lv. + {lv_2} * 2 lv. + {lv_5} * 5 lv. = {money} lv.")