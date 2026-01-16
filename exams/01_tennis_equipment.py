from math import ceil,floor

racket_price = int(input())
shoes_price = racket_price/6
num_rackets = int(input())
num_shoes = int(input())

sum = racket_price*num_rackets + shoes_price*num_shoes
other = 0.2 * sum
sum = sum + other

djokovich_paid = sum / 8
sponsors_paid = sum - djokovich_paid

print(f"Price to be paid by Djokovic {floor(djokovich_paid)}")
print(f"Price to be paid by sponsors {ceil(sponsors_paid)}")
