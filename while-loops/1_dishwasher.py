bottles_detergent = int(input())
detegrent = bottles_detergent * 750

cleaned_dishes = 0
cleaned_pots = 0
used = 0
times = 0

while True:
    command = input()

    if command == "End":
        print(f"Detergent was enough!")
        print(f"{cleaned_dishes} dishes and {cleaned_pots} pots were washed.")
        print(f"Leftover detergent {detegrent} ml.")
        break

    dishes = int(command)
    times += 1

    if times % 3 == 0:
        cleaned_pots += dishes
        used = dishes * 15
    if times % 3 != 0:
        cleaned_dishes += dishes
        used = dishes * 5

    detegrent -= used

    if detegrent < 0:
        print(f"Not enough detergent, {abs(detegrent)} ml. more necessary!")
        break