BANSKO_BOROVETS_EQUIPMENT = 100
BANSKO_BOROVETS_NO_EQUIPMENT = 80
VARNA_BURGAS_BREAKFAST = 130
VARNA_BURGAS_NO_BREAKFAST = 100

VIP_BANSKO_BOROVES_EQUIPMENT = 0.1
VIP_BANSKO_BOROVES_NO_EQUIPMENT = 0.05
VIP_VARNA_BURGAS_BREAKFAST = 0.12
VIP_VARNA_BURGAS_NO_BREAKFAST = 0.07

city = input()
packet = input()
vip = input()
days = int(input())
money = 0
is_valid = True

if days <= 0:
    print(f"Days must be positive number!")
    is_valid = False

if days > 7:
    days -= 1

if (city == "Bansko") or (city == "Borovets"):
    if packet == "noEquipment":
        money += BANSKO_BOROVETS_NO_EQUIPMENT * days
        if vip == "yes":
            money -= money * VIP_BANSKO_BOROVES_NO_EQUIPMENT
    elif packet == "withEquipment":
        money += BANSKO_BOROVETS_EQUIPMENT * days
        if vip == "yes":
            money -= money * VIP_BANSKO_BOROVES_EQUIPMENT
    else:
        is_valid = False
        print(f"Invalid input!")
elif (city == "Varna") or (city == "Burgas"):
    if packet == "noBreakfast":
        money += VARNA_BURGAS_NO_BREAKFAST * days
        if vip == "yes":
            money -= money * VIP_VARNA_BURGAS_NO_BREAKFAST
    elif packet == "withBreakfast":
        money += VARNA_BURGAS_BREAKFAST * days
        if vip == "yes":
            money -= money * VIP_VARNA_BURGAS_BREAKFAST
    else:
        is_valid = False
        print(f"Invalid input!")
else:
    is_valid = False
    print(f"Invalid input!")

if is_valid:
    print(f"The price is {money:.2f}lv! Have a nice time!")