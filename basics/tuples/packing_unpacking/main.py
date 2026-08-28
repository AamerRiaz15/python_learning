students = [
    ("Aisha", 17, (88, 92, 79)),
    ("Leo", 16, (75, 81, 90)),
    ("Maya", 18, (95, 89, 93)),
    ("Zane", 17, (64, 72, 70))
]

student_summary = []
for name, age, (mat, eng, sci) in students:
    avg = (mat + eng + sci) / 3
    student_summary.append((name, avg))

print(student_summary)
