def Select_operation(sign):
    if sign == '+':
        Add()
    elif sign == '-':
        Subtract()
    elif sign == '*':
        Multiply()
    elif sign == '/':
        Divide()

def Add(num1, num2):
    return num1 + num2

def Subtract(num1, num2):
    return num1 - num2

def Multiply(num1, num2):
    return num1 * num2

def Divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        return 'DIVISION ERROR'