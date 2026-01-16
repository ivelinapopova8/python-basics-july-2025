control_num = int(input())

counter = 0
forth_pass = ""

for num_1 in range(1, 10):
    for num_2 in range(1, 10):
        for num_3 in range(1, 10):
            for num_4 in range(1, 10):
                if not num_1 < num_2:
                    continue

                if not num_3 > num_4:
                    continue

                if not num_1 * num_2 + num_3 * num_4 == control_num:
                    continue
                else:
                    counter += 1
                    print(f"{num_1}{num_2}{num_3}{num_4}", end = " ")

                if counter == 4:
                    forth_pass = f"{num_1}{num_2}{num_3}{num_4}"

if counter >= 4:
    print(f"\nPassword: {forth_pass}")
else:
    print("\nNo!")