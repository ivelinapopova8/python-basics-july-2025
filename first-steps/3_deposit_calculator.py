amount_deposited = float(input())
term_of_deposit = int(input())
annual_rate = float(input()) /100

sum = amount_deposited + term_of_deposit * ((amount_deposited * annual_rate) / 12)

print(sum)