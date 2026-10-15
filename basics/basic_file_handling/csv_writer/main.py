import csv

students = [
    ("Aisha", 72),
    ("Ben", 49),
    ("Chloe", 88),
    ("David", 35),
    ("Ella", 91)
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score", "passed"])

    for name, score in students:
        passed = "yes" if score >= 50 else "no"
        writer.writerow([name, score, passed])
