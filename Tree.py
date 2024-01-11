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
        return int(node.value)

    # else evaluate the left and right subtrees
    if node.left:
        left_value = evaluate(node.left)
    if node.right:
        right_value = evaluate(node.right)

    # Perform operation based on the operator this node represents

    #if node.right and not node.left:
    #    if node.value == '~':
    #        return right_value * -1

    #if node.left and not node.right:
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
        #elif char == '!':
        #    t.left = stack.pop()
        #elif char == '~':
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
    prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    op_queue = []
    node_stack = []
    for token in infix:
        if token == '(':
            op_queue.insert(0,token)
        elif token.isdigit():
            node_stack.insert(0,node(token))
        elif token == ')':
            while not op_queue[0] == '(':
                root = node(op_queue[0])
                del op_queue[0]
                root.right = node_stack[0]
                del node_stack[0]
                root.left = node_stack[0]
                del node_stack[0]
                node_stack.insert(0,root)

            del op_queue[0]

        else:
            while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
                root = node(op_queue[0])
                del op_queue[0]
                root.right = node_stack[0]
                del node_stack[0]
                root.left = node_stack[0]
                del node_stack[0]
                node_stack.insert(0, root)

            op_queue.insert(0,token)

    while len(node_stack) > 1:
        root = node(op_queue[0])
        del op_queue[0]
        root.right = node_stack[0]
        del node_stack[0]
        root.left = node_stack[0]
        del node_stack[0]
        node_stack.insert(0, root)

    return node_stack[0]


exp = "5+5+5+5-5"
ans = constructTreeFromInfix(exp)
print(evaluate(ans))