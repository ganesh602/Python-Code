class CalculatorException(Exception):
    pass

def evaluate(formula):
    formula1 = formula.split()

    if len(formula1) != 3:
        raise CalculatorException("Please Provide Poper Format.")

    if formula1[1] == '+':
        Exp = int(formula1[0]) + int(formula1[2])
        return Exp
    elif formula1[1] == '-':
        Exp = int(formula1[0]) - int(formula1[2])
        return Exp
    elif formula1[1] == '*':
        Exp = int(formula1[0]) * int(formula1[2])
        return Exp
    elif formula1[1] == '/':
        Exp = int(formula1[0]) / int(formula1[2])
        return Exp
    elif formula1[1] == '//':
        Exp = int(formula1[0]) // int(formula1[2])
        return Exp
    elif formula1[1] == '%':
        Exp = int(formula1[0]) % int(formula1[2])
        return Exp
    elif formula1[1] == '**':
        Exp = int(formula1[0]) ** int(formula1[2])
        return Exp
    else:
        raise CalculatorException("Please Give Poper Formula eg. +,-,*,%,/,**,// :")

formula = input("Enter Formula e.g 2 * 10 : ")

try:
    print(evaluate(formula))
except CalculatorException as e:
    print(e)

