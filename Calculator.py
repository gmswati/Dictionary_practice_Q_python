# Add
def add(n1,n2):
    return n1+n2

# subtract
def subtract(n1,n2):
    return n1-n2

# multiply
def multiply(n1,n2):
    return n1*n2

# devide
def divide(n1,n2):
    return n1/n2

operations={'+':add,
            '-':subtract,
            '*':multiply,
            '/':divide}

num1= int(input('enter the first number:'))
num2=int(input('enter the second num:'))
