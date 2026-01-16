judges = int(input())
total_grades = 0
total_judges = 0
result = ""

while True:
    project_name = input()

    if project_name == "Finish":
        break

    current_grades = 0

    for count in range(judges):
        grade = float(input())
        current_grades += grade

    result += f"{project_name} - {current_grades / judges:.2f}.\n"
    total_judges += judges
    total_grades += current_grades

result += f"Student's final assessment is {total_grades / total_judges:.2f}."
print(result)


