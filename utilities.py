def strToList(infix):
    '''
    Function converts a string into a list based on operators
    :param infix: string representation of the expression
    :return: list representation of the expression conjoined by operators
    '''
    divided = []
    adder = ""
    numAdded = 0
    point_added = False
    for char in infix:
        if char.isdigit():
            adder += char
            numAdded = 1

        elif char == '.' and numAdded == 1:
            if point_added == True:
                raise SyntaxError("wrong usage of . in number")
            adder += char
            point_added = True

        else:
            numAdded = 0
            if adder != "":
                if adder[-1] == '.' or adder[0] == '.':
                    raise ValueError("wrong representation of float number")
                divided.append(adder)
                adder = ""
            if infix[-1] == '.' or infix[0] == '.':
                raise ValueError("wrong representation of float number")
            divided.append(char)
            point_added = False
    if adder != "":
        divided.append(adder)
    return divided


def sum_of_digits(num):
    '''
    Function calculates the sum of digits of a given number.
    :param num: number to calculate the sum of.
    :return: sum of the number's digits.
    '''
    sum = 0
    while num != "":
        if num[-1] == '.':
            num = num[:-1]
        sum += int(num[-1])
        num = num[:-1]
    return sum


def is_float(string):
    try:
        # Return true if float
        float(string)
        return True
    except ValueError:
        # Return False if Error
        return False


def cleanExpression(infix):
    for ch in infix:
        if ch == ' ' or ch == '\t' or ch == '\n':
            infix = infix.replace(ch, '')
    return infix


def check_for_tilda(is_tilda):
    if is_tilda:
        raise SyntaxError("tilda cannot come before an expression")


def check_for_minus(is_minus):
    if is_minus:
        raise SyntaxError("minus cannot come before an operator")