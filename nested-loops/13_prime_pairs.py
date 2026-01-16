start_first = int(input())
start_second = int(input())
dif_first = int(input())
dif_second = int(input())

end_first = start_first + dif_first
end_second = start_second + dif_second

for pair_1 in range(start_first, end_first + 1):
    is_prime_num1 = True
    if pair_1 < 2:
        is_prime_num1 = False
    else:
        for i in range(2,pair_1):
            if pair_1 % i == 0:
                is_prime_num1 = False
                break
    if not is_prime_num1:
        continue

    for pair_2 in range(start_second, end_second + 1):
        is_prime_num2 = True

        if pair_2 < 2:
            is_prime_num2 = False
        else:
            for j in range(2, pair_2):
                if pair_2 % j == 0:
                    is_prime_num2 = False
                    break
        if not is_prime_num2:
            continue

        print(f"{pair_1}{pair_2}")