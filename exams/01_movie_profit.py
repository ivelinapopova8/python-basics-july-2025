name = input()
days = int(input())
tickets = int(input())
price_ticket = float(input())
perc_cinema = int(input()) / 100

total_sum = days * (price_ticket * tickets)
sum_cinema = total_sum - (total_sum * perc_cinema)

print(f"The profit from the movie {name} is {sum_cinema:.2f} lv.")