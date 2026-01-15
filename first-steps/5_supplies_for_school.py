PRICE_PACKAGES_PENS = 5.80
PRICE_PACKAGES_MARKERS = 7.20
PRICES_PREPARATION = 1.20

packages_pens = int(input())
packages_markers = int(input())
preparation = int(input())
percentage_reduction = int(input()) / 100

total_sum = ((packages_pens * PRICE_PACKAGES_PENS) +
             (packages_markers * PRICE_PACKAGES_MARKERS) +
             (preparation * PRICES_PREPARATION))
total_sum -= (total_sum * percentage_reduction)

print(total_sum)