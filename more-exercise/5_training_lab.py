from math import floor
lenght_w = float(input())
width_h = float(input())
3 <= width_h <= lenght_w <= 100

working_place = 0.7 * 1.2

hall_area = lenght_w * width_h
all_places = (hall_area / working_place) - 3

print(f"{floor(all_places)}")