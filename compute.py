import numpy as np


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def has_x(s):
    return "x" in s or "X" in s


def comp(func, xmin, xmax):
    # ^ is bitwise xor in python, so replace the ^ character with ** for exponents
    func = func.replace('^', '**')

    # define x axis
    x = np.linspace(xmin, xmax, 250)

    # handling constant horizontal line because eval() does not work for that
    
    # if expression is a function of x
    if has_x(func):
        # turn math expression to code
        y = eval(func)
    # else if expression is a numeric constant
    else:
        if is_number(func):
            y = np.array([float(func) for i in range(len(x))])
        # if the expression evaluates to a numeric constant
        else:
            temp = eval(func)
            y = np.array([float(temp) for i in range(len(x))])


    # return axes to be plotted
    return x, y
