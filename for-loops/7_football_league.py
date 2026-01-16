capacity = int(input())
fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for _ in range (fans):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

perc_a = sector_a / fans * 100
perc_b = sector_b / fans * 100
perc_v = sector_v / fans * 100
pers_g = sector_g / fans * 100
all_perc = fans / capacity * 100

print(f"{perc_a:.2f}%")
print(f"{perc_b:.2f}%")
print(f"{perc_v:.2f}%")
print(f"{pers_g:.2f}%")
print(f"{all_perc:.2f}%")
