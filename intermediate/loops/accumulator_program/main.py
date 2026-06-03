accum = 0
count = 0

while True:
    user_input = input('Enter a number or type "done": ')

    if user_input.lower() == 'done':
        break

    try:
        converted_input = float(user_input)
    except:
        print('Invalid Input. Please enter a number.')
        continue

    accum += converted_input
    count += 1
    
average = accum / count

print('Total:', accum)
print('Average:', average)
print('Number of values entered:', count)
