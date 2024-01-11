class node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


def evaluate(node):
    '''
    function receives a node of the syntax tree and recursively evaluates it
    :return: result of evaluation
    '''
    # if the value is a digit, return it as an integer
    if node.value.isdigit():
        return float(node.value)

    # else evaluate the left and right subtrees

    if node.left:
        left_value = evaluate(node.left)
    if node.right:
        right_value = evaluate(node.right)

    # Perform operation based on the operator this node represents

    # if node.right and not node.left:
    #    if node.value == '~':
    #        return right_value * -1

    # if node.left and not node.right:
    #    if node.value == '!':
    #        if left_value >= 0:
    #            result = 1
    #            for idx in range(1, left_value + 1):
    #                result *= idx
    #            return result
    #        else:
    #            raise ValueError("! is an operation on natural numbers")

    if node.left and node.right:
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value
        elif node.value == '^':
            return left_value ** right_value
        elif node.value == '@':
            return float(right_value + left_value) / 2.0
        elif node.value == '$':
            return max(right_value, left_value)
        elif node.value == '&':
            return min(right_value, left_value)
        elif node.value == '%':
            return right_value % left_value
        else:
            raise ValueError("Wrong sons to operator")


def constructTree(postfix):
    stack = []
    for char in postfix:
        t = node(char)
        if char in "+*/^$&%@":
            t1 = stack.pop()
            t2 = stack.pop()
            t.right = t1
            t.left = t2
        # elif char == '!':
        #    t.left = stack.pop()
        # elif char == '~':
        #    t.right = stack.pop()
        elif char == '-':
            if postfix.index(char) == 1:
                t.right = stack.pop()
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                t.right = t1
                t.left = t2
        stack.append(t)
    t = stack.pop()
    return t


def constructTreeFromInfix(infix):
    prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '%': 5, '@': 6, '$': 6, '&': 6}
    op_queue = []
    node_stack = []
    tokenList = strToList(infix)
    print(tokenList)
    for token in tokenList:
        if token == '(':
            op_queue.insert(0, token)
        elif token.isdigit():
            node_stack.insert(0, node(token))
        elif token == ')':
            while not op_queue[0] == '(':
                combine(op_queue, node_stack)

            del op_queue[0]

        else:
            while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
                combine(op_queue, node_stack)

            op_queue.insert(0, token)

    while len(node_stack) > 1:
        combine(op_queue, node_stack)

    return node_stack[0]


def combine(operators, nodes):
    root = node(operators[0])
    del operators[0]
    root.right = nodes[0]
    del nodes[0]
    root.left = nodes[0]
    del nodes[0]
    nodes.insert(0, root)


def expresssionErrors(infix):
    if len(infix) < 1:
        raise ValueError("Empty expression is prohibited")

    token_list = strToList(infix)
    for token in range(len(token_list) - 1):
        if (not token_list[token].isdigit()) and (not token_list[token] in "()+*&^%$@/"):
            raise ValueError("only numbers and operators allowed")

        if token_list[token] in "(+*&^%$@/" and token_list[token + 1] in "+*&^%$@/":
            raise ValueError("No Consecutive operators allowed")

    for token in range(len(token_list)):
        if token_list[token] in "+*&^%$@/" and (token == 0 or token == len(token_list) - 1):
            raise ValueError("wrong use of binary operators")


def strToList(infix):
    divided = []
    adder = ""
    for char in infix:
        if char.isdigit():
            adder += char
        else:
            if adder != "":
                divided.append(adder)
                adder = ""
            divided.append(char)
    if adder != "":
        divided.append(adder)
    return divided


exp = "10+10/2"
expresssionErrors(exp)
ans = constructTreeFromInfix(exp)
print(evaluate(ans))
