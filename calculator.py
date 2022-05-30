import math as m
import os
def calculate(num1, num2, operate):
    '''Calculates num1 and num2 based on the operator'''
    if operate == '+':
        result= num1 + num2
    elif operate == '-':
        result = num1 - num2
    elif operate == '*':
        result = num1 * num2
    elif operate == '/':
        result = num1 / num2
    elif operate == '^':
        result = num1** num2
    elif operate == 'sqrt':
        result = m.sqrt(num1)
    return result

def result(number, operands):
    '''Takes an input number and checks if operator is valid'''
    operation = input(f'Select an operator {operands}: ')
    while operation not in operands:
        operation = input(f' Please choose either of the following: {operands}: ')
    if operation != 'sqrt':
        number2 = float(input(f'{number} {operation} : '))
    else:
        number2 = None
    final_result =  calculate(number,number2, operation)
    print(f' Answer: {final_result}')
    return final_result


print('Calculator')
symbols = '''➕ | ✖ 
➖ | ➗
                
                '''



print(symbols)

operators = '+,-,*,/,^,sqrt'.split(',')

number1 = float(input('Enter a number: '))

new_number = result(number1, operators)


to_repeat = True
while to_repeat:
    choices = ['Y', 'N']
    descison = input(f'Would you like to continue calculating with {new_number}? Y/N: ').upper()
    while descison not in choices:
        descison = input('Please chooose correctly Y/N: ').upper()

    if descison == 'Y':
        new_number = result(new_number, operators)
    else:
        refresh_choices = ['', 'exit']
        refresh = input('Press enter to Clear, type Exit to quit: ').lower()
        while refresh not in refresh_choices:
            refresh = input('Press enter to Clear, type Exit to quit: ').lower()
        if refresh == '':
            os.system('cls')
            number1 = float(input('Enter a number: '))
            new_number = result(number1, operators)
        else:
            print('Goodbye')
            to_repeat = False


