import sys

red = 0
orange = 0
blue = 0
green = 0
max_eggs = -sys.maxsize
max_color = ""
eggs = int(input())

for egg in range (eggs):
    color = input()

    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

if (red > orange) and (red > green) and (red > blue):
    max_eggs = red
    max_color = "red"
elif (orange > green) and (orange > blue):
    max_eggs = orange
    max_color = "orange"
elif green > blue:
    max_eggs = green
    max_color = "green"
else:
    max_eggs = blue
    max_color = "blue"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_color}")
