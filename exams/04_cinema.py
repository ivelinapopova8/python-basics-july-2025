PRICE_TICKET = 5

capacity = int(input())
total_people = 0
is_movie = False
is_full = False
total_sum = 0

while True:
    people_entre = input()
    if people_entre == "Movie time!":
        is_movie = True
        break

    if total_people + int(people_entre) > capacity:
         is_full = True
         break

    total_people += int(people_entre)
    total_sum += int(people_entre) * 5
    if int(people_entre) % 3 == 0:
        total_sum -= 5




if is_full:
    print(f"The cinema is full.")
elif is_movie:
    print(f"There are {capacity - total_people} seats left in the cinema.")

print(f"Cinema income - {total_sum} lv.")