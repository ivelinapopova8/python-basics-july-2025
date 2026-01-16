apartment_size = int(input()) * int(input()) * int(input())

count_boxes = 0
is_done = False

while apartment_size > count_boxes:
    boxes = input()

    if boxes == "Done":
        is_done = True
        break

    count_boxes += int(boxes)

if is_done:
    print(f"{apartment_size - count_boxes} Cubic meters left.")
else:
    print(f"No more free space! You need {count_boxes - apartment_size} Cubic meters more.")