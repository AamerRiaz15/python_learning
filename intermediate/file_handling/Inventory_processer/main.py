import csv

file_name = input('Enter the file name to read data from: ')

if len(file_name) < 1:
    file_name = 'inventory2.csv'

items = []
try:
    with open(file_name, 'r', newline='') as md:
        reader = csv.reader(md)
        header = next(reader)
        
        for row in reader:
            if not row:
                continue

            item, quantity, price = row
            quantity = int(quantity)
            price = float(price)
            total_value = quantity * price
            items.append([item, quantity, price, round(total_value, 2)])

    with open('inventory_updated.csv', 'w', newline='') as md_2:
        writer = csv.writer(md_2)
        writer.writerow(['Item', 'Quantity', 'Price', 'Total value'])
        writer.writerows(items)
except Exception as e:
    print(f'Something went wrong: {e}')
    quit()

print('Success! Data written to "inventory_updated.csv".')
