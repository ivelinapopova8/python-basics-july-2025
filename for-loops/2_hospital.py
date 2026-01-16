period = int(input())

doctors = 7
yes_patients = 0
no_patients = 0
day = 1

for days in range(period):
    patients = int(input())

    if doctors >= patients:
        yes_patients += patients
        day += 1
    else:
        no_patients += patients - doctors
        yes_patients += doctors
        day += 1
    if day % 3 == 0:
        if no_patients > yes_patients:
            doctors += 1

print(f"Treated patients: {yes_patients}.")
print(f"Untreated patients: {no_patients}.")
