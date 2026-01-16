LARGE_RED = 16
LARGE_GREEN = 12
LARGE_YELLOW = 9
MEDIUM_RED = 13
MEDIUM_GREEN = 9
MEDIUM_YELLOW = 7
SMALL_RED = 9
SMALL_GREEN = 8
SMALL_YELLOW = 5

size = input()
color = input()
num = int(input())
price = 0

if size == "Large":
    if color == "Red":
        price = LARGE_RED * num
    elif color == "Green":
        price = LARGE_GREEN * num
    elif color == "Yellow":
        price = LARGE_YELLOW * num
elif size == "Medium":
    if color == "Red":
        price = MEDIUM_RED * num
    elif color == "Green":
        price = MEDIUM_GREEN * num
    elif color == "Yellow":
        price = MEDIUM_YELLOW * num
elif size == "Small":
    if color == "Red":
        price = SMALL_RED * num
    elif color == "Green":
        price = SMALL_GREEN * num
    elif color == "Yellow":
        price = SMALL_YELLOW * num

price -= price * 0.35
print(f"{price:.2f} leva.")