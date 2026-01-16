first_num = int(input())
second_num = int(input())

for num in range(first_num, second_num + 1):
    even_sum = 0
    odd_sum = 0

    for index, value in enumerate(str(num)):
        if index % 2 == 0:
            even_sum += int(value)
        elif index % 2 != 0:
            odd_sum += int(value)

    if even_sum == odd_sum:
        print(num, end = " ")


