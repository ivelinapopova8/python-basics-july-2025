QUARTER_STANDARD = 55.50
QUARTER_PREMIUM = 105.20
QUARTER_VIP = 118.90
SEMI_STANDARD = 75.88
SEMI_PREMIUM = 125.22
SEMI_VIP = 300.40
FINAL_STANDARD = 110.10
FINAL_PREMIUM = 160.66
FINAL_VIP = 400
photo_trophy = 40

DISCOUNT_2500 = 0.10
DISCOUNT_4000 = 0.25

level = str(input())
type = str(input())
num_tickets = int(input())
photo = str(input())
price = 0

if level == "Quarter final":
    if type == "Standard":
        price = QUARTER_STANDARD * num_tickets
    elif type == "Premium":
        price = QUARTER_PREMIUM * num_tickets
    elif type == "VIP":
        price = QUARTER_VIP * num_tickets
elif level == "Semi final":
    if type == "Standard":
        price = SEMI_STANDARD * num_tickets
    elif type == "Premium":
        price = SEMI_PREMIUM * num_tickets
    elif type == "VIP":
        price = SEMI_VIP * num_tickets
elif level == "Final":
    if type == "Standard":
        price = FINAL_STANDARD * num_tickets
    elif type == "Premium":
        price = FINAL_PREMIUM * num_tickets
    elif type == "VIP":
        price = FINAL_VIP * num_tickets

if price > 4000:
    price = price - (price * DISCOUNT_4000)
    photo_trophy = 0
elif price > 2500:
    price = price - (price * DISCOUNT_2500)

if photo == "Y":
    price += photo_trophy * num_tickets

print(f"{price:.2f}")
