import sys


def read_number(expr):
    try:
        num = int(expr)
    except ValueError:
        print('Введите число!')
        sys.exit(1)
    assert num >= 0, 'Операнд должен быть неотрицательным'
    return num


def read_expression_str():
    a = input('Введите выражение: ')
    expression = a.split()
    assert len(expression) == 3, 'Неверное количество аргументов!'
    return expression


def parse_arguments(expression):
    oper = expression[0]
    num1 = read_number(expression[1])
    num2 = read_number(expression[2])
    return oper, num1, num2


def evaluate_expression(oper, num1, num2):
    operation = ['+', '-', '*', '/']
    assert oper in operation, 'Недопустимая операция'
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print('Нельзя делить на ноль!')
            sys.exit(1)
    print(result)

evaluate_expression(*parse_arguments(read_expression_str()))













