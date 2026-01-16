PRICE_MUSSELS = 7.50

price_mackerel = float(input())
price_sprinkle = float(input())
kg_bonito = float(input())
kg_safrid = float(input())
kg_mussels = float(input())

PRICE_BONITO = 1.60 * price_mackerel
PRICE_SAFRID = 1.80 * price_sprinkle

sum = ((PRICE_BONITO * kg_bonito) +
       (PRICE_SAFRID * kg_safrid) +
       (kg_mussels * PRICE_MUSSELS))
print(f"{sum:.2f}")