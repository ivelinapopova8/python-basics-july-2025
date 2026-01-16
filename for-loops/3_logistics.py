PRICE_MICROBUSS_TON = 200
PRICE_TRUCK_TON = 175
PRICE_TRAIN_TON = 120

total_tons = 0
sum = 0
micr_tons = 0
truck_tons = 0
train_tons = 0

tovars = int(input())

for _ in range(tovars):
    tons_per_tovar = int(input())

    if tons_per_tovar <= 3:
        micr_tons += tons_per_tovar
        sum += PRICE_MICROBUSS_TON * tons_per_tovar
    elif 4 <= tons_per_tovar <= 11:
        truck_tons += tons_per_tovar
        sum += PRICE_TRUCK_TON * tons_per_tovar
    elif tons_per_tovar >= 12:
        train_tons += tons_per_tovar
        sum += PRICE_TRAIN_TON * tons_per_tovar

sum_tons = micr_tons + truck_tons + train_tons
avr_price_per_ton = sum / sum_tons
perc_micr = micr_tons / sum_tons * 100
perc_truck = truck_tons / sum_tons * 100
perc_train = train_tons / sum_tons * 100

print(f"{avr_price_per_ton:.2f}")
print(f"{perc_micr:.2f}%")
print(f"{perc_truck:.2f}%")
print(f"{perc_train:.2f}%")