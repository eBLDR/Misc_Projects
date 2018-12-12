#! /usr/bin/python3
# By eBLDR

import os

import sympy as sp


def get_integer(min_, max_, prompt):
    """
    Gets user's input, validates integer in range
    :param min_: minimum value
    :param max_: maximum value
    :param prompt: message to display
    :return: integer validated
    """
    while True:
        user_input = input('%s [%i,%i]: ' % (prompt, min_, max_))
        if user_input.isdigit():
            user_input = int(user_input)
            if min_ <= user_input <= max_:
                return user_input
        print('Invalid input.')


def create_polynomial():
    degree = get_integer(0, 20, '> Degree of the polynomial')
    sp.var('x')
    coefficients = sp.symbols('a0:%i' % (degree + 1))
    polynomial = sp.sympify('0')
    for n, a in enumerate(coefficients):
        polynomial = polynomial + a * x ** n
    
    for n, a in enumerate(coefficients):
        coef_value = get_integer(MIN, MAX, '> Coefficient of a_%i' % n)
        if coef_value:
            polynomial = polynomial.subs(a, coef_value)
    return polynomial


def delete(p):
    p = sp.sympify('0')
    return p


def evaluate(z):
    a = get_integer(MIN, MAX, '> Lower limit')
    if not a:
        a = sp.var("a")
    t = z.subs(x, a)
    t = sp.sympify(t)
    return t


def solve(z):
    t = sp.solve(z, x)
    t = sp.simplify(t)
    input('Roots of P(x): {}\n<enter>'.format(t))


def swap(z, y):
    return y, z


def add(z, y):
    return z + y


def subtract(z, y):
    return z - y


def product(z, y):
    return z * y


def derivative(z):
    t = sp.diff(z, x)
    return t


def integrate(z):
    t = sp.integrate(z, x)
    return t


def definite_integrate(z):
    c = get_integer(MIN, MAX, '> Lower limit')
    d = get_integer(MIN, MAX, '> Upper limit')
    if not c:
        c = sp.var('c')
    if not d:
        d = sp.var('d')
    t = sp.integrate(z, (x, c, d))
    return t


def graph(z):
    e = get_integer(MIN, MAX, '> Lower limit')
    f = get_integer(MIN, MAX, '> Upper limit')
    if not e:
        e = 0
    if not f:
        f = 100
    try:
        sp.plot(z, (x, e, f))
    except:
        input('Invalid data.\n<enter>')


def menu(var1, var2):
    cmd = ''
    while cmd != 'e':
        os.system('clear')
        display_menu(var1, var2)
        cmd = input('> Action: ')
        if cmd in ['e', 'E']:
            print('Exited!')
        elif cmd == '0':
            var1 = delete(var1)
        elif cmd == '1':
            var1 = create_polynomial()
        elif cmd == '2':
            (var1, var2) = swap(var1, var2)
        elif cmd == '3':
            var2 = evaluate(var1)
        elif cmd == '4':
            var2 = add(var1, var2)
        elif cmd == '5':
            var2 = subtract(var1, var2)
        elif cmd == '6':
            var2 = product(var1, var2)
        elif cmd == '7':
            var2 = derivative(var1)
        elif cmd == '8':
            var2 = integrate(var1)
        elif cmd == '9':
            var2 = definite_integrate(var1)
        elif cmd == 'r':
            solve(var1)
        elif cmd == 'g':
            graph(var2)
        else:
            print('Invalid option.')
    return var1, var2


def display_menu(var1, var2):
    print('''### POLYNOMIAL CALCULATOR ###
0 - Delete P(x)
1 - Set P(x)
2 - P(x) <-> Q(x)
3 - Evaluate P(a)
4 - Q(x) = P(x) + Q(x)
5 - Q(x) = P(x) - Q(x)
6 - Q(x) = P(x) * Q(x)
7 - Q(x) = Derivative P(x)
8 - Q(x) = Integrate P(x)
9 - Q(x) = Integrate Definite P(x)
r - Solve P(x) = 0
g - Graph of Q(x)
e - EXIT
===============
P(x) = {}
Q(x) = {}
==============='''.format(var1, var2))


def main():
    sp.var('x')
    p, q = 0, 0
    p, q = menu(p, q)


if __name__ == '__main__':
    MAX = 1000
    MIN = -MAX
    main()
