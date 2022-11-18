def sumNum(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multy(num1, num2):
    return num1 * num2


def root(num1, num2):
    if num1 == 0:
        return 0.0
    if num2 < 0:
        return (num2 * -1) ** (1 / num1)
    return num2 ** (1 / num1)


def division(num1, num2):
    if num2 == 0:
        return "Err, you can't divide by 0"
    return num1 / num2


def percent(num1, num2):
    # num1 % of num2, like 25 % 100 = 4
    return (num1 / 100) * num2
