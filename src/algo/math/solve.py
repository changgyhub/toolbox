"""
Numerical methods for solving equations f(x) = 0.
"""


def newton1D(f, x_0, df=None, delta=0.00001):
    """
    Find solution to f(x) = 0 with newton's method
    :param f: function f
    :param x_0: starting point for x
    :param df: first order derivative of f
    :param delta: threshold for solution
    :return: x
    """
    x_n = x_0
    if df is None:
        from sympy import diff, symbols, lambdify
        x = symbols('x')
        df = lambdify(x, diff(f(x), x))
    while True:
        x_n1 = x_n - f(x_n) / df(x_n)
        if abs(x_n - x_n1) < delta:
            return x_n1
        x_n = x_n1


def bisection1D(f, a, b, delta=0.00001):
    """
    Find solution to f(x) = 0 with bisection method
    :param f: function f
    :param a: left starting point for x
    :param b: right starting point for x
    :param delta: threshold for solution
    :return: x
    """
    start, end = a, b
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    elif f(a) * f(b) > 0:
        print("couldn't find root in [{}, {}], return {}".format(a, b, None))
        return None
    else:
        mid = (start + end) / 2
        while abs(start - mid) > delta:
            if f(mid) == 0:
                return mid
            elif f(mid) * f(start) < 0:
                end = mid
            else:
                start = mid
            mid = (start + end) / 2
        return mid


def intersection1D(f, x0, x1, delta=0.00001):
    """
    Find solution to f(x) = 0 with intersection method
    :param f: function f
    :param x0: first starting point of x
    :param x1: second starting point of x
    :param delta: threshold for solution
    :return: x
    """
    x_n, x_n1 = x0, x1
    while True:
        x_n2 = x_n1 - f(x_n1) / ((f(x_n1) - f(x_n)) / (x_n1 - x_n))
        if abs(x_n2 - x_n1) < delta:
            return x_n2
        x_n = x_n1
        x_n1 = x_n2


if __name__ == "__main__":

    def f1(x):
        return x**3-2*x-5

    def df1(x):
        return 3*(x**2)-2

    print(newton1D(f1, 3))
    print(newton1D(f1, 3, df1))
    print(bisection1D(f1, 1, 3))
    print(intersection1D(f1, 3, 3.5))
