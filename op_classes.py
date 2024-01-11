MAX_FLOAT = 1.7976931348623157e+308
class Operator:
  def __init__(self, isBinary, canComeBefore):
    self.isBinary = True
    self.canComeBefore
    self.canComeAfter


class AddOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return float(token1) + float(token2)

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Tokens need to be numeric: +")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Number too big for operation: +")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: +")

        return True

class MulOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return float(token1) * float(token2)

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Tokens need to be numeric: *")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Number too big for operation: *")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: *")

        return True

class DivOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return float(token1) / float(token2)

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Tokens need to be numeric: /")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Number too big for operation: /")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: /")
        if float(token2) == 0:
            raise ValueError("Cannot divide by 0: /")

        return True

class PowOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return float(token1) ** float(token2)

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Tokens need to be numeric: ^")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT or float(token1) ** float(token2) > MAX_FLOAT:
            raise ValueError("Numbers or their result is too big: ^")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: ^")

        return True

class AvgOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return (float(token1) + float(token2)) / 2.0

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Tokens need to be numeric: @")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Numbers or their result is too big: @")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: @")

        return True

class MaxOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return max(float(token1), float(token2))

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Tokens need to be numeric: $")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Numbers or their result is too big: $")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: $")

        return True

class MinOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return min(float(token1), float(token2))

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Tokens need to be numbers: &")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Numbers or their result is too big: &")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: &")

        return True

class ModOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(str)
        canComeAfter = type(str)

    def action(self, token1, token2):
        return float(token1) % float(token2)

    def possibleErrors(self, token1, token2):
        temp_token1 = str(token1).replace('.', '', 1)
        temp_token2 = str(token2).replace('.', '', 1)
        if (not temp_token1.isdigit()) or (not temp_token2.isdigit()):
            raise TypeError("Token needs to be a number: %")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Numbers or their result is too big: %")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: %")

        return True

class NegOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = False
        canComeBefore = type(str)
        canComeAfter = type(Operator)

    def action(self, token1):
        return 0 - float(token1)

    def possibleErrors(self, token1):
        temp_token = str(token1).replace('.','',1)
        if not temp_token.isdigit():
            raise TypeError("Token needs to be a number: ~")
        if float(token1) > MAX_FLOAT:
            raise ValueError("Number or their result is too big: ~")
        if isinstance(token1, Operator):
            raise TypeError("action only works on non-operators: ~")

        return True

class facOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = False
        canComeBefore = type(Operator)
        canComeAfter = type(str)

    def action(self, token1):
        factorial = 1
        for idx in range(2,token1):
            factorial *= idx
        return factorial


    def possibleErrors(self, token1):
        if not str(token1).isnumeric():
            raise TypeError("Token need to be numeric (natural): !")
        if int(token1) > 100:
            raise ValueError("Number or their result is too big: !")
        if isinstance(token1, Operator):
            raise TypeError("action only works on non-operators: !")

        return True