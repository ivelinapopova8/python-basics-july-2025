EXPENSE_WATER = 20
EXPENSE_INTERNET = 15

months = int(input())
sum_electricity = 0
sum_others = 0

for _ in range(months):
     expense_electricity = float(input())

     expense_others = (EXPENSE_WATER + EXPENSE_INTERNET + expense_electricity) * 1.20

     sum_electricity += expense_electricity
     sum_others += expense_others

sum_water = EXPENSE_WATER * months
sum_internet = EXPENSE_INTERNET * months
total_sum = sum_electricity + sum_others + sum_water + sum_internet
avrg = total_sum / months

print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {sum_others:.2f} lv")
print(f"Average: {avrg:.2f} lv")
