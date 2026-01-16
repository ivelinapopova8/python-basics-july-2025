people_musala = 0
people_monblan = 0
people_kilimanjaro = 0
people_k2 = 0
people_everest = 0
sum_all = 0

groups = int(input())

for _ in range(groups):
    num_people = int(input())
    sum_all += num_people

    if num_people <= 5:
        people_musala += num_people
    elif 6 <= num_people <= 12:
        people_monblan += num_people
    elif 13 <= num_people <= 25:
        people_kilimanjaro += num_people
    elif 26 <= num_people <= 40:
        people_k2 += num_people
    elif num_people >= 41:
        people_everest += num_people

perc_musala = people_musala / sum_all * 100
perc_monblan = people_monblan / sum_all * 100
perc_kilimanjaro = people_kilimanjaro / sum_all * 100
perc_k2 = people_k2 / sum_all * 100
perc_everest = people_everest / sum_all * 100

print(f"{perc_musala:.2f}%")
print(f"{perc_monblan:.2f}%")
print(f"{perc_kilimanjaro:.2f}%")
print(f"{perc_k2:.2f}%")
print(f"{perc_everest:.2f}%")

