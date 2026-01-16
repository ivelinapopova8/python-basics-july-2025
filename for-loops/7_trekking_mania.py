groups = int(input())

num_musala = 0
num_monblan = 0
num_kilimanjaro = 0
num_k2 = 0
num_everest = 0

for _ in range(groups):
     people_in_group = int(input())

     if people_in_group <= 5:
         num_musala += people_in_group
     elif 6 <= people_in_group <= 12:
         num_monblan += people_in_group
     elif 13 <= people_in_group <= 25:
         num_kilimanjaro += people_in_group
     elif 26 <= people_in_group <= 40:
         num_k2 += people_in_group
     elif people_in_group >= 41:
         num_everest += people_in_group

sum_people = num_musala + num_monblan + num_k2 + num_kilimanjaro + num_everest

perc_musala = num_musala / sum_people * 100
perc_monblan = num_monblan / sum_people * 100
perc_kilimanjaro = num_kilimanjaro / sum_people * 100
perc_k2 = num_k2 / sum_people * 100
perc_everest = num_everest / sum_people * 100

print(f"{perc_musala:.2f}%")
print(f"{perc_monblan:.2f}%")
print(f"{perc_kilimanjaro:.2f}%")
print(f"{perc_k2:.2f}%")
print(f"{perc_everest:.2f}%")