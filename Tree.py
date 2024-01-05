class node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        self.operator = False


def evaluate(node):
    '''
    function receives a node of the syntax tree and recursively evaluates it
    :return: result of evaluation
    '''
    # if the value is a digit, return it as an integer
    if node.value.isdigit():
        return int(node.value)

    # else evaluate the left and right subtrees
    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    # Perform operation based on the operator this node represents
    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        return left_value // right_value
    elif node.value == '^':
        return right_value ** left_value
    elif node.value == '@':
        return float(right_value + left_value) / 2.0
    elif node.value == '$':
        return max(right_value, left_value)
    elif node.value == '&':
        return min(right_value, left_value)
    elif node.value == '%':
        return right_value % left_value
    elif node.value == '~':
        return right_value * -1
    elif node.value == '!':
        result = 1
        for idx in range(1, left_value + 1):
            result *= idx
        return result
    else:
        raise ValueError("Unknown operator")
