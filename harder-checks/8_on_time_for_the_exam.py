hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())

minutes_exam += hour_exam * 60
minutes_arrive += hour_arrive * 60

time = minutes_exam - minutes_arrive
hours = abs(time) // 60
minutes = abs(time) % 60

if 0 <= time <= 30:
    print(f"On time")
    if time != 0:
        print(f"{minutes} minutes before the start")
elif time > 30:
    print(f"Early")
    if hours > 0:
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{minutes} minutes before the start")
elif time < 0:
    print(f"Late")
    if hours > 0:
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{minutes} minutes after the start")

