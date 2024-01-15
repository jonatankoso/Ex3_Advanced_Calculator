class node:
    def __init__(self, value):
        '''
        Function builds a tree node based on given value
        :param value: data of node
        '''
        self.left = None
        self.value = value
        self.right = None

    def clone(self):
        '''
        Function clones a tree node
        :return: clone of given node
        '''
        n = node(self.value)
        n.left = None if self.left is None else self.left.clone()
        n.right = None if self.right is None else self.right.clone()
        return n


def evaluate(node):
    '''
    function receives a node of the expression tree and recursively evaluates it
    :return: result of evaluation
    '''
    # if the value is a digit, return it as an integer
    if node.value.isdigit() or is_float(node.value):
        return float(node.value)

    # else evaluate the left and right subtrees
    if node.left:
        left_value = evaluate(node.left)
    if node.right:
        right_value = evaluate(node.right)

    # Perform operation based on the operator this node represents
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
            return left_value % right_value
        elif node.value == '~':
            return 0 - right_value
        elif node.value == '#':
            return sum_of_digits(str(right_value))
        elif node.value == '_':
            return 0 - right_value

        elif node.value == '!':
            if float(right_value).is_integer() and right_value > 0:
                result = 1
                for idx in range(1, int(right_value) + 1):
                    result *= idx
                return result
            else:
                raise ValueError("! is an operation on natural numbers")

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
    '''
    Function constructs an expression tree from given equation
    :param infix: str representation of the equation
    :return: expression tree representing the equation
    '''

    # Setting precedence of operators
    prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '%': 5, '@': 6, '$': 6, '&': 6, '_': 7, '!': 7, '~': 7, '#': 7}
    op_queue = []
    node_stack = []
    tokenList = strToList(infix)
    print(tokenList)    # Check for mistakes in converting expression to list
    open_paren_count_stack = []
    last_unary_prefix_seen_stack = []
    open_operand_count = 0

    # check for each one of 4 options for token, '(', number, operator, ')'
    for token in tokenList:
        # check for 1st option, if token is (
        if token == '(':
            op_queue.insert(0, token)

            # Check for parenthesis after ~ (what expression to negate)
            if len(open_paren_count_stack) > 0:
                open_paren_count_stack[0] += 1

        # check for 2nd option, if token is number
        elif token.isdigit() or is_float(token):
            open_operand_count += 1
            node_stack.insert(0, node(token))

            # if ~ (or any other prefix unary operator) comes before the current expression (number in this case)
            while len(open_paren_count_stack) > 0 and open_paren_count_stack[0] == 0:
                # code dup
                while len(op_queue) > 0 and prec[op_queue[0]] >= prec[last_unary_prefix_seen_stack[0]]:
                    combine(op_queue, node_stack)

                node_stack.insert(0, node_stack[0].clone())
                op_queue.insert(0, last_unary_prefix_seen_stack[0])
                del last_unary_prefix_seen_stack[0]
                del open_paren_count_stack[0]

        # check for 3rd option, ')'
        elif token == ')':
            # combine the operator and operands into one expression
            while not op_queue[0] == '(':
                combine(op_queue, node_stack)
            del op_queue[0]

            # if any unary operator came before the (, make sure to reduce the number of open parenthesis after it
            if len(open_paren_count_stack) > 0:
                open_paren_count_stack[0] -= 1

                # if the unary operation needs to be executed on the closed expression
                while len(open_paren_count_stack) > 0 and open_paren_count_stack[0] == 0:
                    # code dup
                    while len(op_queue) > 0 and prec[op_queue[0]] >= prec[last_unary_prefix_seen_stack[0]]:
                        combine(op_queue, node_stack)

                    node_stack.insert(0, node_stack[0].clone())
                    op_queue.insert(0, last_unary_prefix_seen_stack[0])
                    del last_unary_prefix_seen_stack[0]
                    del open_paren_count_stack[0]

        # check for 4th option, operator
        else:
            # # if a new operator with lower precedence is inserted, combine the previous expression
            # while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
            #     combine(op_queue, node_stack)

            # special case for prefix unary expressions
            if token == '~' or (token == '-' and open_operand_count == 0):
                if token != '~':
                    token = '_' # fix to unary minus
                # if a new operator with lower precedence is inserted, combine the previous expression
                while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
                    combine(op_queue, node_stack)
                last_unary_prefix_seen_stack.insert(0, token)
                open_paren_count_stack.insert(0, 0)
            # special case for postfix unary expressions
            elif token == '!' or token == '#':
                # if a new operator with lower precedence is inserted, combine the previous expression
                while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
                    combine(op_queue, node_stack)
                node_stack.insert(0, node_stack[0].clone())
                op_queue.insert(0, token)
            else: # binary operator
                # if a new operator with lower precedence is inserted, combine the previous expression
                while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
                    combine(op_queue, node_stack)
                op_queue.insert(0, token)
                open_operand_count -= 1

    # if any last expression left
    while len(node_stack) > 1:
        combine(op_queue, node_stack)

    return node_stack[0]


def combine(operators, nodes):
    '''
    Functions merges the operator and it's operands into an expression tree
    :param operators: operators stack (contains recent operators)
    :param nodes: nodes stack (contains recent operands)
    :return: node with the operator as root and the operands as leaves
    '''
    root = node(operators[0])
    del operators[0]
    root.right = nodes[0]
    del nodes[0]
    root.left = nodes[0]
    del nodes[0]
    nodes.insert(0, root)


def expresssionErrors(infix):
    '''
    Function finds general mistakes in the expression itself
    :param infix: string representation of the expression
    :return: none
    '''
    if len(infix) < 1:
        raise ValueError("Empty expression is prohibited")

    token_list = strToList(infix)
    for token in range(len(token_list) - 1):
        if (not token_list[token].isdigit()) and (not is_float(token_list[token])) and (not token_list[token] in "()+*&^%$@/!~#-"):
            raise ValueError("only numbers and operators allowed")

        if token_list[token] in "(+*&^%$@/~" and token_list[token + 1] in "+*&^%$@/":
            raise ValueError(
                "No Consecutive operators of such kind allowed: " + token_list[token] + " " + token_list[token + 1])

    for token in range(len(token_list)):
        if token_list[token] in "+*&^%$@/" and (token == 0 or token == len(token_list) - 1):
            raise ValueError("wrong use of binary operators")

        if (token_list[token] in '~-' and token == len(token_list) - 1) or (token_list[token] in '!#' and token == 0):
            raise ValueError("wrong use of unary operators")


def strToList(infix):
    '''
    Function converts a string into a list based on operators
    :param infix: string representation of the expression
    :return: list representation of the expression conjoined by operators
    '''
    divided = []
    adder = ""
    numAdded = 0
    for char in infix:
        if char.isdigit():
            adder += char
            numAdded = 1

        elif char == '.' and numAdded == 1:
            adder += char

        else:
            numAdded = 0
            if adder != "":
                if adder[-1] == '.' or adder[0] == '.':
                    raise ValueError("wrong representation of float number")
                divided.append(adder)
                adder = ""
            divided.append(char)
    if adder != "":
        divided.append(adder)
    return divided


def sum_of_digits(num):
    '''
    Function calculates the sum of digits of a given number
    :param num: number to calculate the sum of
    :return: sum of the number's digits
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


#exp = "(5*2+~3!)!"
exp = "~-5.1"
expresssionErrors(exp)
ans = constructTreeFromInfix(exp)
print(evaluate(ans))
