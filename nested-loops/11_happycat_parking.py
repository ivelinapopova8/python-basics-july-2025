days = int(input())
hours = int(input())
total_sum = 0

for day in range(1, days + 1):
    tax_day = 0
    for hour in range(1, hours + 1):
        if (day % 2 == 0) and (hour % 2 != 0):
            current_tax = 2.50
        elif (day % 2 == 1) and (hour % 2 == 0):
            current_tax = 1.25
        else:
            current_tax = 1

        tax_day += current_tax
        total_sum += current_tax
    print(f"Day: {day} - {tax_day:.2f} leva")
print(f"Total: {total_sum:.2f} leva")