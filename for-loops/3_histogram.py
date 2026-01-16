numbers = int(input())

total_p1 = 0
total_p2 = 0
total_p3 = 0
total_p4 = 0
total_p5 = 0

for _ in range(numbers):
    num = int(input())

    if num < 200:
        total_p1 += 1
    elif 200 <= num <= 399:
        total_p2 += 1
    elif 400 <= num <= 599:
        total_p3 += 1
    elif 600 <= num <= 799:
        total_p4 += 1
    else:
        total_p5 += 1

perc_p1 = total_p1 / numbers * 100
perc_p2 = total_p2 / numbers * 100
perc_p3 = total_p3 / numbers * 100
perc_p4 = total_p4 / numbers * 100
perc_p5 = total_p5 / numbers * 100

print(f"{perc_p1:.2f}%")
print(f"{perc_p2:.2f}%")
print(f"{perc_p3:.2f}%")
print(f"{perc_p4:.2f}%")
print(f"{perc_p5:.2f}%")
