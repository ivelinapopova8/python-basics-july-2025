time_photos = int(input())
num_scenes = int(input())
time_scene = int(input())

preparing = 0.15 * time_photos
time_photos -= preparing
need_time = num_scenes * time_scene

if need_time <= time_photos:
    print(f"You managed to finish the movie on time! You have {round(time_photos - need_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(need_time - time_photos)} minutes.")