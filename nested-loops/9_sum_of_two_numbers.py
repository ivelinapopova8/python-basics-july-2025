start = int(input())
end = int(input())
magic_num = int(input())

counter = 0
is_found = False

for num_1 in range(start, end + 1):
    for num_2 in range(start, end + 1):
        sum = num_1 + num_2
        counter += 1

        if sum == magic_num:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{counter} ({num_1} + {num_2} = {magic_num})")
else:
    print(f"{counter} combinations - neither equals {magic_num}")