class node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        self.operator = False


def evaluate(node) -> int:
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