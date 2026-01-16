FINE_FACEBOOK = 150
FINE_INSTAGRAM = 100
FINE_REDDIT = 50

numbers = int(input())
salary = int(input())

for _ in range(numbers):
    tabs = input()

    if tabs == "Facebook":
        salary -= FINE_FACEBOOK
    elif tabs == "Instagram":
        salary -= FINE_INSTAGRAM
    elif tabs == "Reddit":
        salary -= FINE_REDDIT

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(f"{salary}")