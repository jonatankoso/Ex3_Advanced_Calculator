class Operator:
  def __init__(self, isBinary, canComeBefore):
    self.isBinary = True
    self.canComeBefore
    self.canComeAfter


class AddOp:
    def __init__(self, isBinary, canComeBefore, canComeAfter):
        isBinary = True
        canComeBefore = type(int)
        canComeAfter = type(int)

    def action(self, token1, token2):
        return int(token1) + int(token2)

    def possibleErrors(self, token1, token2):
        if not str(token1).isnumeric() or str(token1).isnumeric():
            raise TypeError("Tokens need to be numeric: +")
        if int(token1) > 4294967296 or int(token2) > 4294967296:
            raise ValueError("Number too big for operation: +")
        if isinstance(token1, Operator) or isinstance(token2, Operator):
            raise TypeError("action only works on non-operators: +")

        return 1
