#! /usr/bin/python3
# By eBLDR

import os
import sys


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


# Menu actions
def delete():
    return 0


def set_():
    variable = get_integer(MIN, MAX, '> Value of A: ')
    return variable


def swap(x, y):
    return y, x


def negate(x):
    return -x


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def product(x, y):
    return x * y


def division(x, y):
    return x / y


def remainder(x, y):
    return x % y


def power(x, y):
    return x ** y


def calculator(var1, var2):
    cmd = ''
    
    while cmd != 'e':
        os.system('clear')
        display_menu(var1, var2)
        cmd = input('> Action: ')
        
        if cmd in ['e', 'E']:
            print('Exited!')
            sys.exit()
        elif cmd == '0':
            var1 = delete()
        elif cmd == '1':
            var1 = set_()
        elif cmd == '2':
            var1, var2 = swap(var1, var2)
        elif cmd == '3':
            var2 = negate(var1)
        elif cmd == '4':
            var2 = add(var1, var2)
        elif cmd == '5':
            var2 = subtract(var1, var2)
        elif cmd == '6':
            var2 = product(var1, var2)
        elif cmd == '7':
            var2 = division(var1, var2)
        elif cmd == '8':
            var2 = remainder(var1, var2)
        elif cmd == '9':
            var2 = power(var1, var2)
        else:
            print('Invalid option.')
    
    return var1, var2


def display_menu(var1, var2):
    print('''#### CALCULATOR ####
0 - delete A
1 - set A
2 - A <-> B
3 - B = -A
4 - B = A + B
5 - B = A - B
6 - B = A * B
7 - B = A / B
8 - B = A % B
9 - B = A ** B
e - Exit
===============
A = {}
B = {}
==============='''.format(var1, var2))


if __name__ == '__main__':
    MAX = 1000
    MIN = -MAX
    A, B = 0, 0
    A, B = calculator(A, B)
