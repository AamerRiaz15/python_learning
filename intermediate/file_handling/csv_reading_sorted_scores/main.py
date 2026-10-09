import csv

passed_students = []

with open('students.csv', 'r') as md:
    reader = csv.DictReader(md)
    for row in reader:
        if row['passed'] == 'yes':
            passed_students.append(row)

sorted_passed = sorted(
    passed_students,
    key=lambda s: int(s['score']),
    reverse=True
)

print('------Student Summary------')
for student in passed_students:
    print(student['name'], student['score'])
