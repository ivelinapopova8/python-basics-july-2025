name = input()
num_tickets_adults = int(input())
num_tickets_kids = int(input())
net_price_adults = float(input())
service_tax = float(input())

money = (num_tickets_adults * net_price_adults) + (num_tickets_adults * service_tax)
money += (num_tickets_kids * (net_price_adults * 0.3)) + (num_tickets_kids * service_tax)
win_money = money * 0.2

print(f"The profit of your agency from {name} tickets is {win_money:.2f} lv.")