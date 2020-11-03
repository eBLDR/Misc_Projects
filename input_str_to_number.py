def separator():
    print('\n' + ('=' * 30) + '\n')


def get_integer_1():
    while True:
        output_number = ''
        number_type = int
        number = input("Number: ")

        if len(number) == 0:
            print("Input something...")
            continue

        if number.count('.') > 1:
            continue

        elif number.count('.') == 1:
            number_type = float

        number = number.replace(',', '')  # Accept ',' as thousand separator

        for i in number:
            if i not in '0123456789.':
                break
            output_number += i

        else:
            return number_type(output_number)

        print("Invalid input")


integer = get_integer_1()
print(integer)
print(type(integer))

separator()


def get_integer_2():
    while True:
        number = input("Number: ")
        for i in number:
            if i not in '0123456789':
                break
        else:
            if len(number) != 0:
                return int(number)

        print("Invalid input")


integer = get_integer_2()
print(integer)
print(type(integer))

separator()


# Control variable
def get_integer_3():
    while True:
        number = input("Number: ")
        is_int = True
        for i in number:
            if i not in '0123456789':
                is_int = False
                break

        if is_int and len(number) != 0:
            return int(number)

        print("Invalid input")


integer = get_integer_3()
print(integer)
print(type(integer))

separator()


# try/except method
def get_integer_4():
    while True:
        number = input("Number: ")
        try:
            return int(number)
        except ValueError:
            try:
                return float(number)
            except ValueError:
                print("Invalid input")


integer = get_integer_4()
print(integer)
print(type(integer))

separator()


# .isdigit() method
def get_integer_5():
    while True:
        number = input("Number: ")
        if number.isdigit():
            return int(number)

        print("Invalid input")


integer = get_integer_5()
print(integer)
print(type(integer))
