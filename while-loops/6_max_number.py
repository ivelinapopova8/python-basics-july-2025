import sys

max_number = -sys.maxsize

comand = input()

while comand != "Stop":
    num = int(comand)
    if num > max_number:
        max_number = num
    comand = input()
print(max_number)