students = int(input())

grade_2 = 0
grade_3 = 0
grade_4 = 0
grade_5_6 = 0
total_grades = 0

for _ in range(students):
    grade = float(input())

    if 2 <= grade <= 2.99:
        total_grades += grade
        grade_2 += 1
    elif 3 <= grade <= 3.99:
        total_grades += grade
        grade_3 += 1
    elif 4 <= grade <= 4.99:
        total_grades += grade
        grade_4 += 1
    elif grade >= 5:
        total_grades += grade
        grade_5_6 += 1

perc_5_6 = grade_5_6 / students * 100
perc_4 = grade_4 / students * 100
perc_3 = grade_3 / students * 100
perc_2 = grade_2 / students * 100
avr_grade = total_grades / students

print(f"Top students: {perc_5_6:.2f}%")
print(f"Between 4.00 and 4.99: {perc_4:.2f}%")
print(f"Between 3.00 and 3.99: {perc_3:.2f}%")
print(f"Fail: {perc_2:.2f}%")
print(f"Average: {avr_grade:.2f}")

