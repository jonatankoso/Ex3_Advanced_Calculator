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
        if not str(token1).isnumeric() or str(token1).isnumeric():
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
        if not str(token1).isnumeric() or str(token1).isnumeric():
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
        if not str(token1).isnumeric() or str(token1).isnumeric():
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
        if not str(token1).isnumeric() or str(token1).isnumeric():
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
        if not str(token1).isnumeric() or str(token1).isnumeric():
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
        if not str(token1).isnumeric() or str(token1).isnumeric():
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
        if not str(token1).isnumeric() or str(token1).isnumeric():
            raise TypeError("Tokens need to be numeric: &")
        if float(token1) > MAX_FLOAT or float(token2) > MAX_FLOAT:
            raise ValueError("Numbers or their result is too big: &")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: &")

        return True