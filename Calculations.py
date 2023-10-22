def Add(num1, num2):
    return int(num1) + int(num2)

def Subtract(num1, num2):
    return int(num1) - int(num2)

def Multiply(num1, num2):
    return int(num1) * int(num2)

def Divide(num1, num2):
    try:
        return int(num1) / int(num2)
    except ZeroDivisionError as e:
        return 'NIE KURWA PRZEZ 0'
    
def calculate(values):
    result = 0
    if len(values) >= 3:
        if values[1] == '+':
            result = Add(values[0], values[2])
        elif values[1] == '-':
            result = Subtract(values[0], values[2])
        elif values[1] == '*':
            result = Multiply(values[0], values[2])
        elif values[1] == '/':
            result = Divide(values[0], values[2])
        return result