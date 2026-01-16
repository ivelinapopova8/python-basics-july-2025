min_kontr = int(input())
sec_kontr = int(input())
length_meters = float(input())
sek_100m = int(input())

sec_kontr = min_kontr * 60 + sec_kontr
time_marin = (length_meters / 100)* sek_100m
times_delay = length_meters / 120
time_marin = time_marin - times_delay* 2.5

if time_marin <= sec_kontr:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_marin:.3f}.")
else:
    print(f"No, Marin failed! He was {time_marin-sec_kontr:.3f} second slower.")