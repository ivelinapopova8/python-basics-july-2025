record_seconds = float(input())
distance_meters = float(input())
time_seconds_1_meter = float(input())

distance = distance_meters * time_seconds_1_meter
delay = (distance_meters // 15 ) * 12.5
ivan_record = distance + delay

if ivan_record < record_seconds:
    print(f"Yes, he succeeded! The new world record is {ivan_record:.2f} seconds.")
elif ivan_record >= record_seconds:
    print(f"No, he failed! He was {abs(record_seconds - ivan_record):.2f} seconds slower.")