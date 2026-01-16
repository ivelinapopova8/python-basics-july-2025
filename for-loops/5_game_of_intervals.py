NUM_0_9 = 0.20
NUM_10_19 = 0.30
NUM_20_29 = 0.40
NUM_30_39 = 50
NUM_40_50 = 100

moves = int(input())

points = 0
num_0_9 = 0
num_10_19 = 0
num_20_29 = 0
num_30_39 = 0
num_40_50 = 0
invalid_nums = 0

for _ in range(moves):
    number = int(input())

    if 0 <= number <= 9:
        points += NUM_0_9 * number
        num_0_9 += 1
    elif 10 <= number <= 19:
        points += NUM_10_19 * number
        num_10_19 += 1
    elif 20 <= number <= 29:
        points += NUM_20_29 * number
        num_20_29 += 1
    elif 30 <= number <= 39:
        points += NUM_30_39
        num_30_39 += 1
    elif 40 <= number <= 50:
        points += NUM_40_50
        num_40_50 += 1
    elif (number > 50) or (number < 0):
        invalid_nums += 1
        points = points / 2

perc_0_9 = num_0_9 / moves * 100
perc_10_19 = num_10_19 / moves * 100
perc_20_29 = num_20_29 / moves * 100
perc_30_39 = num_30_39 / moves * 100
perc_40_50 = num_40_50 / moves * 100
perc_invalid = invalid_nums / moves * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {perc_0_9:.2f}%")
print(f"From 10 to 19: {perc_10_19:.2f}%")
print(f"From 20 to 29: {perc_20_29:.2f}%")
print(f"From 30 to 39: {perc_30_39:.2f}%")
print(f"From 40 to 50: {perc_40_50:.2f}%")
print(f"Invalid numbers: {perc_invalid:.2f}%")
