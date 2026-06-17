item = input('Enter an item to buy: ')
quantity = int(input('Enter quantity: '))
price = float(input('Enter price: '))

row = {
    "Item": item,
    "Quantity": quantity,
    "Price": price
}

file_name = input('Enter the file that you would like to write to: ')

if len(file_name) < 1:
    file_name = 'purchases.csv'

try:
    file_handle = open(file_name, 'w')
    file_handle.write('Item,Quantity,Price\n')
    file_handle.write(f'{row["Item"]},{row["Quantity"]},{row["Price"]}\n')
    file_handle.close()
except Exception as e:
    print(f'Something went wrong: {e}')
    exit()

print(f'Success! Data written to {file_name}')
