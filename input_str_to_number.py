def separator():
    print('\n' + ('=' * 30) + '\n')


# long method #1
while True:
    outputNumber = ''
    numberType = 'i'
    dotCount = 0  # to make sure that the float can be understood
    number = input("Number: ")
    if len(number) == 0:
        print("Input something...")
        continue
    for i in number:
        if i not in '0123456789.,':
            break
        elif i == ',':  # to accept ',' thousand separators
            continue
        else:
            if i == '.':  # to accept floats
                dotCount += 1
                if dotCount > 1:
                    break
                numberType = 'f'
            outputNumber += i
    else:
        if numberType == 'i':
            outputNumber = int(outputNumber)
        else:
            outputNumber = float(outputNumber)
        break
    print("Invalid input")

print(outputNumber)
print(type(outputNumber))

# long method #1 version B
separator()

while True:
    number = input("Number: ")
    for i in number:
        if i not in '0123456789':
            break
    else:
        if len(number) != 0:
            number = int(number)
            break
    print("Invalid input")

print(number)
print(type(number))

# long method #2 using control variable
separator()

while True:
    number = input("Number: ")
    isInt = True
    for i in number:
        if i not in '0123456789':
            isInt = False
            break
    if isInt and len(number) != 0:
        number = int(number)
        break
    print("Invalid input")

print(number)
print(type(number))

# try/except method
separator()

while True:
    number = input("Number: ")
    try:
        outputNumber = int(number)
        break
    except:
        try:
            outputNumber = float(number)
            break
        except:
            pass
    print("Invalid input")

print(outputNumber)
print(type(outputNumber))

# .isdigit() method
separator()

while True:
    number = input("Number: ")
    if number.isdigit():
        outputNumber = int(number)
        break
    print("Invalid input")

print(outputNumber)
print(type(outputNumber))
