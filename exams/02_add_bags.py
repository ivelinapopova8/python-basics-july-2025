price_over20 = float(input())
kg_baggage = float(input())
days = int(input())
num_baggages = int(input())

price_less10 = 0.2 * price_over20
price_1020 = 0.5 * price_over20
money = 0

if days < 7:
    if kg_baggage < 10:
        money += (price_less10 * 1.4) * num_baggages
    elif 10 <= kg_baggage <= 20:
        money += (price_1020 * 1.4) * num_baggages
    elif kg_baggage > 20:
        money += (price_over20 * 1.4) * num_baggages
elif 7 <= days <= 30:
    if kg_baggage < 10:
        money += (price_less10 * 1.15) * num_baggages
    elif 10 <= kg_baggage <= 20:
        money += (price_1020 * 1.15) * num_baggages
    elif kg_baggage > 20:
        money += (price_over20 * 1.15) * num_baggages
elif days > 30:
    if kg_baggage < 10:
        money += (price_less10 * 1.1) * num_baggages
    elif 10 <= kg_baggage <= 20:
        money += (price_1020 * 1.1) * num_baggages
    elif kg_baggage > 20:
        money += (price_over20 * 1.1) * num_baggages

print(f"The total price of bags is: {money:.2f} lv. ")