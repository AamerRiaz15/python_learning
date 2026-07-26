def add(a, b):
    calculation = a + b
    return calculation

def subtract(a, b):
    calculation = a - b
    return calculation

def multiply(a, b):
    calculation = a * b
    return calculation

def divide(a, b):
    if b == 0:
        print('Error. Division by zero attempted.')
        return None
    
    calculation = a / b
    return calculation

def calculate():
    try:
        choice1 = float(input('Enter a number: '))
        choice2 = float(input('Enter another number: '))
        operator = input('Enter an operator: ')
    except ValueError:
        print(f'Invalid input.')
        exit()

    if operator == '+':
        return add(choice1, choice2)
    elif operator == '-':
        return subtract(choice1, choice2)
    elif operator == '*':
        return multiply(choice1, choice2)
    elif operator == '/':
        return divide(choice1, choice2)
    else:
        print('Invalid input.')   
        return None

answer = calculate()
print(answer)
