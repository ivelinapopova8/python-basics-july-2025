length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

aquarium_volume = length * width * height
aquarium_volume -= (aquarium_volume * percentage)
total_volume = aquarium_volume / 1000

print(total_volume)