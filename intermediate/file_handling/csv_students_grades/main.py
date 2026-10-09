import csv

passed_students = []

with open("students.csv", "r") as md:
    reader = csv.DictReader(md)
    for student in reader:
        if student["passed"] == "yes":
            passed_students.append(student)

print("------Students who passed------")
for student in passed_students:
    print(student["name"], student["score"])
