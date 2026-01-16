from importlib.metadata import pass_none
from math import pi

radius = float(input())

calculated_area = pi * radius * radius
calculated_perimeter = 2 * pi * radius

print(f"{calculated_area:.2f}")
print(f"{calculated_perimeter:.2f}")