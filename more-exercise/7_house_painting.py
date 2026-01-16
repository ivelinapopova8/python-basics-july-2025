LITTER_GREEN_PAINT = 3.4
LITTER_RED_PAINT = 4.3

height_house_x = float(input())
weight_house_y = float(input())
height_roof_h = float(input())

side_green = height_house_x * weight_house_y
window = 1.5 * 1.5
two_sides = (2 * side_green) - (2 * window)
front_green = height_house_x * height_house_x
door = 2 * 1.2
two_fronts = (2 * front_green) - door
green_area = two_sides + two_fronts
green_paint = green_area / LITTER_GREEN_PAINT

sides_red = 2 * (height_house_x * weight_house_y)
triangles_red = 2 * (height_house_x * height_roof_h / 2)
red_area = sides_red + triangles_red
red_paint = red_area / LITTER_RED_PAINT

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")