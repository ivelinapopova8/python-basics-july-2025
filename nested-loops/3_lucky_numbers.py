n = int(input())

for num_1 in range(1, 10):

    for num_2 in range(1, 10):

        for num_3 in range(1, 10):

            for num_4 in range(1, 10):
                sum_first = num_1 + num_2
                sum_second = num_3 + num_4
                if (sum_first == sum_second) and (n % sum_first == 0):
                    print(f"{num_1}{num_2}{num_3}{num_4}", end = " ")
