from math import ceil
import sys

PACKET_FLOAR = 750
PACKET_SUGAR = 950

kozunaci = int(input())
need_floar = 0
need_sugar = 0
max_flour = -sys.maxsize
max_sugar = -sys.maxsize

for _ in range(kozunaci):
    sugar = int(input())
    floar = int(input())

    need_sugar += sugar
    need_floar += floar
    if sugar > max_sugar:
        max_sugar = sugar
    if floar > max_flour:
        max_flour = floar

packets_sugar = (need_sugar / PACKET_SUGAR)
packets_floar = (need_floar / PACKET_FLOAR)

print(f"Sugar: {ceil(packets_sugar)}")
print(f"Flour: {ceil(packets_floar)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")