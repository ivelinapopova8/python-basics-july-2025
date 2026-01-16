num_people = int(input())

back = 0
chest = 0
legs = 0
abbs = 0
protein_shake = 0
protein_bar = 0
train_people = 0
protein_people = 0

for i in range(num_people):
    exercise = str(input())

    if exercise == "Back":
        back += 1
        train_people += 1
    elif exercise == "Chest":
        chest += 1
        train_people += 1
    elif exercise == "Legs":
        legs += 1
        train_people += 1
    elif exercise == "Abs":
        abbs += 1
        train_people += 1
    elif exercise == "Protein shake":
        protein_shake += 1
        protein_people += 1
    elif exercise == "Protein bar":
        protein_bar += 1
        protein_people += 1

perc_train = (train_people / num_people) * 100
perc_protein = (protein_people / num_people) * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abbs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{perc_train:.2f}% - work out")
print(f"{perc_protein:.2f}% - protein")
