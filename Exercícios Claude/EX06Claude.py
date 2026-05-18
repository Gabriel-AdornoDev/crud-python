def somar(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b
a = int(input('Valor 1: '))
b = int(input('Valor 2: '))

oper = input("Operação (+, -, *, /): ")
if oper == '+':
    print(somar(a, b))
elif oper == '-':
    print(sub(a, b))
elif oper == '*':
    print(mult(a,b))
else:
    print(div(a,b))