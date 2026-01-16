last_sector = input()
num_rows_in_A = int(input())
num_seats_odd = int(input())

num_seats = 0

for sector_code in range(ord("A"), ord(last_sector) + 1):
    sector = chr(sector_code)

    current_rows = num_rows_in_A + (sector_code - ord('A'))

    for row_code in range(1, current_rows + 1):

        if row_code % 2 == 0:
            current_seat = num_seats_odd + 2
        elif row_code % 2 != 0:
            current_seat = num_seats_odd

        for seat_code in range(current_seat):
            seat = chr(ord("a")  + seat_code)
            num_seats += 1

            print(f"{sector}{row_code}{seat}")
print(num_seats)
