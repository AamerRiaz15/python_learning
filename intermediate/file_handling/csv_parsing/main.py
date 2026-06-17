try:
    file_name = input('Enter the file name with the extension: ').strip()

    if len(file_name) < 1:
        file_name = 'sample.csv'

    file_handle = open(file_name, 'r')
    lines = file_handle.readlines()
    file_handle.close()
except Exception as e:
    print(f'Something went wrong: {e}')
    exit()

headers = lines[0]
formatted_headers = headers.strip().split(',')
print(formatted_headers)

list1 = []

for line in lines[1:]:
    line = line.strip()

    if not line:
        continue

    parts = line.split(',')

    item = parts[0]
    quantity = int(parts[1])
    price = float(parts[2])
    line_total = quantity * price


    row = {
        "Item": item,
        "Quantity": quantity,
        "Price": price,
        "Line total": line_total
    }

    list1.append(row)

print('---Summary---')
for row in list1:
    item = row["Item"]
    quantity = row["Quantity"]
    price = row["Price"]
    line_total = row["Line total"]

    print(f'{item} - {quantity} x {price:.2f} = {line_total:.2f}')
