while True:
    try:
        user_input = input('Enter a number between 1 and 10: ')
        num = float(user_input)
    except Exception as e:
        print('Invalid input! Please try again.')
        continue

    if num < 1 or num > 10:
        print('Please try again.')
        continue
    else:
        print(f'You chose: {num}. Goodbye.')
        break
