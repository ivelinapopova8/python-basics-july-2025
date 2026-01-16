wanted_book = input()
tries = 0
checked_book = input()

while checked_book != wanted_book and checked_book != "No More Books":
    tries += 1
    checked_book = input()

if checked_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {tries} books.")
elif checked_book == wanted_book:
    print(f"You checked {tries} books and found it.")