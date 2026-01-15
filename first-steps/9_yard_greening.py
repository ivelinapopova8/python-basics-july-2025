area = float(input())
price_of_1_kvm = 7.61
discount = 0.18
price_of_area = price_of_1_kvm*area
price_discount = price_of_area*discount
final_prize = price_of_area-price_discount
print(f"The final price is: {final_prize} lv.")
print(f"The discount is: {price_discount} lv.")