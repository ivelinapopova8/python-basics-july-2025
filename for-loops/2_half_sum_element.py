import sys

numbers = int(input())

max_number = -sys.maxsize
sum = 0

for _ in range(numbers):
    num = int(input())

    if num > max_number:
        max_number = num

    sum += num

half_sum = sum - max_number

if half_sum == max_number:
    print(f"Yes\nSum = {half_sum}")
else:
    print(f"No\nDiff = {abs(half_sum - max_number)}")