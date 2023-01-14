students_grades = {}

n = int(input())

for _ in range(n):
    student, grade = input().split()

    if student not in students_grades.keys():
        students_grades[student] = []

    students_grades[student].append(float(grade))

for key in students_grades.keys():
    print(key, end=" -> ")
    print(" ".join(map(lambda st: f'{st:.2f}', students_grades.get(key))), end=" ")

    avg = sum(students_grades.get(key)) / len(students_grades.get(key))
    print(f'(avg: {avg:.2f})')
