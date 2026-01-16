max_stot = int(input())
max_des = int(input())
max_ed = int(input())

for stot in range(1, max_stot + 1):
    for des in range(1, max_des + 1):
        for ed in range(1, max_ed + 1):
            if (ed % 2 != 0) or (stot % 2 != 0):
                continue

            if not des in [2, 3, 5, 7]:
                continue

            print(f"{stot} {des} {ed}")