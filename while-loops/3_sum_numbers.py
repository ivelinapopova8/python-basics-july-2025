number = int(input())
sum = 0

while True:
    new_number = int(input())
    sum += new_number

    if sum >= number:
        print(sum)
        break