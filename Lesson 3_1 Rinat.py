def my_div():
    print('This is the function for dividing one argument by another')
    try:
        arg1 = float(input('Enter first argument: '))
        arg2 = float(input('Enter second argument: '))
        result = arg1 / arg2
    except ZeroDivisionError:
        return 'You cannot divide by zero!'
    except ValueError:
        return 'Inappropriate argument value!'
    return f'{result:.2f}'

print (f'Result {my_div()}')
