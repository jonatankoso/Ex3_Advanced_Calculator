def str_to_list(infix: str) -> list:
    """
    Function converts a string into a list based on operators
    :param infix: string representation of the expression
    :return: list representation of the expression conjoined by operators
    """
    divided = []
    adder = ""
    num_added = 0
    point_added = False
    for char in infix:
        if char.isdigit():
            adder += char
            num_added = 1

        # case number is not whole
        elif char == '.' and num_added == 1:
            if point_added:
                raise SyntaxError("wrong usage of . in number")
            adder += char
            point_added = True

        else:
            num_added = 0
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


def sum_of_digits(num: str) -> int:
    """
    Function calculates the sum of digits of a given number.
    :param num: number to calculate the sum of.
    :return: sum of the number's digits.
    """
    sum_digits = 0
    if 'e' in num:
        num = num[:num.index('e')]
    while num != "":
        if num[-1] == '.':
            num = num[:-1]
        sum_digits += int(num[-1])
        num = num[:-1]
    return sum_digits


def is_float(string: str) -> bool:
    """
    Function checks if a number is a float expression
    :param string: "float" number in question
    :return: True if the number is a float, else False
    """
    try:
        # Return true if float
        float(string)
        return True
    except ValueError:
        # Return False if Error
        return False


def clean_expression(infix: str) -> str:
    """
    Function skips over white spaces in the expression.
    :param infix: expression that may contain white spaces.
    :return: expression without white spaces.
    """
    for ch in infix:
        if ch == ' ' or ch == '\t' or ch == '\n':
            infix = infix.replace(ch, '')
    return infix


def check_for_tilda(is_tilda: bool):
    """
    Function checks the case where a tilda "~" comes before an expression or operator, which is prohibited
    :param is_tilda: True or False based on placement of tilda in operation
    :return: none
    """
    if is_tilda:
        raise SyntaxError("tilda cannot come before an expression")


def check_for_minus(is_minus: bool):
    """
    Function checks the case where a unary minus "-" comes before an operator, which is prohibited
    :param is_minus: True or False based on placement of minus in operation
    :return: none
    """
    if is_minus:
        raise SyntaxError("minus cannot come before an operator")
