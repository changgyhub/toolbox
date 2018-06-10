"""
Numerical integration.
"""


def next_step(a, b, h):
    x = a + h
    while x < (b - h):
        yield x
        x = x + h


def trapezoidal(left, right, steps):
    """
    Trapezoidal Rule: int(f) = h/2 * (f1 + 2f2 + ... + fn)
    :param left: left end of searching range
    :param right: right end of searching range
    :param steps: steps for searching
    :return: int(f)
    """
    a, b = left, right
    h = (b - a) / steps
    y = 0
    y += (h / 2) * f(a)
    for i in next_step(a, b, h):
        y += h * f(i)
    y += (h / 2) * f(b)
    return y


def simpson(left, right, steps):
    """
    Simpson's Rule: int(f) = h/2 * (b-a)/3*(f1 + 4f2 + 2f_3 + ... + fn)
    :param left: left end of searching range
    :param right: right end of searching range
    :param steps: steps for searching
    :return: int(f)
    """
    a, b = left, right
    h = (b - a) / steps
    y = 0
    y += (h / 3) * f(a)
    cnt = 2
    for i in next_step(a, b, h):
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i)
        cnt += 1
    y += (h / 3) * f(b)
    return y


if __name__ == '__main__':

    def f(x):
        return x ** 2


    print(trapezoidal(0, 3, 100))
    print(simpson(0, 3, 100))
