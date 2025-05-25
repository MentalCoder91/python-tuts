def cal_grades(marks):
    if 91 <= marks <= 100:
        return "Outstanding"
    elif 81 <= marks <= 90:
        return "Exceeds"
    elif 71 <= marks <= 80:
        return "Acceptable"
    else:
        return "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for student in student_scores:
    student_grades[student] = cal_grades(student_scores[student])

print(student_grades)
