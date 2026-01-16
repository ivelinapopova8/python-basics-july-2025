record = float(input())
meters = float(input())
time_sec = float(input())

times_delay = meters // 50
time_georgi = meters * time_sec + times_delay * 30

if time_georgi >= record:
    print(f"No! He was {time_georgi - record:.2f} seconds slower.")
elif time_georgi < record:
    print(f"Yes! The new record is {time_georgi:.2f} seconds.")