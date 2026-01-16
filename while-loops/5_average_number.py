num = int(input())
sum = 0

for _ in range(num):
    number = int(input())
    sum += number

avg = sum / num
print(f"{avg: .2f}")
