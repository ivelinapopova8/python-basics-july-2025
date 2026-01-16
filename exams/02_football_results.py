result1 = str(input())
result2 = str(input())
result3 = str(input())

won = 0
lost = 0
draw = 0

a1,b1 = result1.split(":")
a1 = int(a1)
b1 = int(b1)
if a1 > b1:
    won += 1
elif a1 < b1:
    lost += 1
else:
    draw += 1

a2,b2= result2.split(":")
a2 = int(a2)
b2 = int(b2)
if a2 > b2:
    won += 1
elif a2 < b2:
    lost += 1
else:
    draw += 1

a3,b3= result3.split(":")
a3 = int(a3)
b3 = int(b3)
if a3 > b3:
    won += 1
elif a3 < b3:
    lost += 1
else:
    draw += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")