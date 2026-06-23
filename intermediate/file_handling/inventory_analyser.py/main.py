import csv

file_name = input('Enter the file name with the extension: ')

if len(file_name) < 1:
    file_name = 'inventory_old.csv'

line_total_list = []
items = []

try:
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if not row:
                continue
            
            item = row[0]
            quantity = int(row[1])
            price = float(row[2])
            line_total = quantity * price

            line_total_list.append(line_total)
            items.append([item, quantity, price, line_total])
except Exception as e:
    print(f'Something went wrong: {e}')
    quit()

sum = 0
for i in line_total_list:
    sum += i

highest_price = items[0][2]
most_expensive_item = items[0][0]
for item, quantity, price, line_total in items:
    if price > highest_price:
        highest_price = price
        most_expensive_item = item

lowest_price = items[0][2]
least_expensive_item = items[0][0]
for item, quantity, price, line_total in items:
    if price < lowest_price:
        lowest_price = price
        least_expensive_item = item

print('---Least expensive item---')
print(least_expensive_item, lowest_price)

print('---Most Expensive Item---')
print(most_expensive_item, highest_price)

print("---Sum---")
print(sum)
