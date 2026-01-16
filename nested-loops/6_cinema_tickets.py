all_students = 0
all_standards = 0
all_kids = 0
result = ""

while True:
    film_name = input()

    if film_name == "Finish":
        break

    able_seats = int(input())
    sold_tickets = 0

    while sold_tickets < able_seats:
        type_ticket = input()

        if type_ticket == "End":
            break

        if type_ticket == "student":
            all_students += 1
        elif type_ticket == "standard":
            all_standards += 1
        elif type_ticket == "kid":
            all_kids += 1

        sold_tickets += 1

    result += f"{film_name} - {sold_tickets / able_seats * 100:.2f}% full.\n"

total_tickets = all_students + all_standards + all_kids
result += (f"Total tickets: {total_tickets}\n"
           f"{all_students / total_tickets * 100:.2f}% student tickets.\n"
           f"{all_standards / total_tickets * 100:.2f}% standard tickets.\n"
           f"{all_kids / total_tickets * 100:.2f}% kids tickets.\n")
print(result)


