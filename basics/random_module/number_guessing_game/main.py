import random

rand_num = random.randint(1, 100)

guesses = 0

while True:
    guesses += 1
    choice = input('Guess the number between 1 and 100: ')

    try:
        converted_choice = int(choice)
    except Exception as e:
        print(f'Invalid input. Try again.')
        continue
    if converted_choice == rand_num:
        print(f'Well done! you got the answer in {guesses} guesses.')
        break
    elif converted_choice < rand_num:
        print('Too low!')
    elif converted_choice > rand_num:
        print('Too high!')
