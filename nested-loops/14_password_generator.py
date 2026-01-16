n = int(input())
l = int(input())

for num1 in range(1, n + 1):
    for num2 in range(1, n + 1):
        for let1 in range(ord("a"), ord("a") + l):
            for let2 in range(ord("a"), ord("a") + l):
                for num3 in range(1, n + 1):
                    if (num3 <= num1) or (num3 <= num2):
                        continue
                    print(f"{num1}{num2}{chr(let1)}{chr(let2)}{num3}", end = " ")