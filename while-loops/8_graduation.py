name = input()
grade = 1
score = 0
falid_times = 0

while True:
    new_score = float(input())
    if new_score < 4.00:
        falid_times += 1
        if falid_times > 1:
            print(f"{name} has been excluded at {grade} grade")
            break
        continue

    score += new_score
    if grade == 12:
        avg_score = score / 12
        print(f"{name} graduated. Average grade: {avg_score:.2f}")
        break
    grade += 1