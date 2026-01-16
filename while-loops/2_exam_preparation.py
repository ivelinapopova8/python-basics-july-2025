bad_grades_limit = int(input())
count_bad_grades = 0
count_problems = 0
count_grades = 0
last_problem = ""
has_failed = True

while count_bad_grades < bad_grades_limit:
    name_task = input()

    if name_task == "Enough":
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        count_bad_grades += 1

    count_grades += grade
    count_problems += 1
    last_problem = name_task

if has_failed:
    print(f"You need a break, {count_bad_grades} poor grades.")
else:
    print(f"Average score: {count_grades / count_problems:.2f}")
    print(f"Number of problems: {count_problems}")
    print(f"Last problem: {last_problem}")
