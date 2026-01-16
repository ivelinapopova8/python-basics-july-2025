num_students = 0
num_standard = 0
num_kids = 0
is_finish = False

while True:
    name = input()
    if name == "Finish":
        is_finish = True
        break

    free_seats = int(input())
    num_seats = 0

    while free_seats > 0:
        type_seat = input()
        if type_seat == "End":
            break

        if type_seat == "student":
            num_students += 1
        elif type_seat == "standard":
            num_standard += 1
        elif type_seat == "kid":
            num_kids += 1

        num_seats +=1
        free_seats -= 1

    perc = 0
    if free_seats == 0:
        perc = 100
    else:
        perc = (num_seats/(num_seats + free_seats)) * 100

    print(f"{name} - {perc:.2f}% full.")

if is_finish:
    all_tickets = num_kids + num_standard + num_students
    print(f"Total tickets: {num_kids + num_students + num_standard}")
    print(f"{(num_students/all_tickets)*100:.2f}% student tickets.")
    print(f"{(num_standard/all_tickets)*100:.2f}% standard tickets.")
    print(f"{(num_kids/all_tickets)*100:.2f}% kids tickets.")

