import csv

salary_total = []

with open('employees.csv', 'r') as md:
    reader = csv.DictReader(md)

    print('#####################################')
    print('------Employees and Departments------')
    for row in reader:
        print(row['name'], row['department'])
        salary_total.append(int(row['salary']))
    print('#####################################')

salary_sum = sum(salary_total)

print('#####################################')
print('----------Combined salaries----------')
print(salary_sum)
print('#####################################')
