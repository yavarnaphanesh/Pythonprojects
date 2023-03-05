# Student Scores Grading

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Darco": 74,
    "Neville": 62,
}

student_grades = {}

for i in student_scores:
    if student_scores[i] >= 91:
        student_grades[i] = "Outstanding"
    elif student_scores[i] >= 81 and student_scores[i] <= 90:
        student_grades[i] = "Exceeds Expectation"
    elif student_scores[i] >= 71 and student_scores[i] <= 80:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"
print(student_grades)
