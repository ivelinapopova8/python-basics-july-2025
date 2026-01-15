PRICE_VIDEOCARD = 250

budget = float(input())
videocards = int(input())
processors = int(input())
rams = int(input())

sum_videocards = videocards * PRICE_VIDEOCARD
PRICE_PROCESSOR = sum_videocards * 0.35
PRICE_RAM = sum_videocards * 0.10

sum = ((videocards * PRICE_VIDEOCARD) +
       (processors * PRICE_PROCESSOR) +
       (rams * PRICE_RAM))

if videocards > processors:
    sum -= sum * 0.15

if sum <= budget:
    print(f"You have {budget - sum:.2f} leva left!")
elif sum > budget:
    print(f"Not enough money! You need {sum - budget:.2f} leva more!")