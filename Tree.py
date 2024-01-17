import utilities
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
    left_value = 0
    right_value = 0
    # if the value is a digit, return it as an integer
    if node.value.isdigit() or utilities.is_float(node.value):
        return float(node.value)

    # else evaluate the left and right subtrees
    if node.left:
        left_value = evaluate(node.left)
    if node.right:
        right_value = evaluate(node.right)

    # Perform operation based on the operator this node represents
    if node.left and node.right:
        if isinstance(right_value, complex) or isinstance(left_value, complex):
            raise TypeError("number cannot be complex")
        right_value = round(right_value, 10)
        left_value = round(left_value, 10)
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value
        elif node.value == '^':
            if left_value == 0 and right_value <= 0:
                raise ZeroDivisionError("0 can only be brought by positive power")
            return left_value ** right_value
        elif node.value == '@':
            return float(right_value + left_value) / 2.0
        elif node.value == '$':
            return max(right_value, left_value)
        elif node.value == '&':
            return min(right_value, left_value)
        elif node.value == '%':
            if right_value == 0:
                raise ValueError("cannot modulo by 0")
            return left_value % right_value
        elif node.value == '~':
            return right_value * -1
        elif node.value == '#':
            if left_value >= 0:
                return utilities.sum_of_digits(str(right_value))
            raise ValueError("# only works on positive numbers")
        elif node.value == '_':
            return 0 - right_value
        elif node.value == '|':
            return 0 - right_value

        elif node.value == '!':
            if float(right_value).is_integer() and right_value >= 0:
                result = 1
                for idx in range(1, int(right_value) + 1):
                    result *= idx
                return result
            else:
                raise ValueError("! is an operation on natural numbers")

        else:
            raise ValueError("Wrong sons to operator")


def constructTreeFromInfix(infix):
    '''
    Function constructs an expression tree from given equation
    :param infix: str representation of the equation
    :return: expression tree representing the equation
    '''

    # Setting precedence of operators
    prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '|': 4.5, '%': 5, '@': 6, '$': 6, '&': 6, '!': 7, '~': 7,
            '#': 7, '_': 8}
    op_queue = []
    node_stack = []
    tokenList = utilities.strToList(infix)
    print(tokenList)  # Check for mistakes in converting expression to list
    open_paren_count_stack = []
    last_unary_prefix_seen_stack = []
    open_operand_count = 0
    prev_token = ""
    minus_first_checker = 1
    tilda_before = False
    minus_before = False

    # check for each one of 4 options for token, '(', number, operator, ')'
    for token in tokenList:
        # check for 1st option, if token is (
        if token == '(':
            tilda_before = False
            minus_before = False
            minus_first_checker = 1
            op_queue.insert(0, token)

            # Check for parenthesis after ~ (what expression to negate)
            if len(open_paren_count_stack) > 0:
                open_paren_count_stack[0] += 1

        # check for 2nd option, if token is number
        elif token.isdigit() or utilities.is_float(token):
            tilda_before = False
            minus_before = False
            minus_first_checker = 0
            open_operand_count += 1
            node_stack.insert(0, node(token))

            # if ~ (or any other prefix unary operator) comes before the current expression (number in this case)
            while len(open_paren_count_stack) > 0 and open_paren_count_stack[0] == 0:
                # code dup
                while (len(op_queue) > 0 and prec[op_queue[0]] >= prec[last_unary_prefix_seen_stack[0]] and op_queue[0]
                       != last_unary_prefix_seen_stack[0] == '|'):
                    combine(op_queue, node_stack)

                node_stack.insert(0, node_stack[0].clone())
                op_queue.insert(0, last_unary_prefix_seen_stack[0])
                del last_unary_prefix_seen_stack[0]
                del open_paren_count_stack[0]

        # check for 3rd option, ")"
        elif token == ')':
            tilda_before = False
            minus_before = False
            minus_first_checker = 0
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
            # special case for prefix unary expressions
            if token == '~' or (token == '-' and open_operand_count == 0):
                if token != '~':
                    tilda_before = False
                    if (prev_token == "" or prev_token == '(') or (prev_token in '-_|' and minus_first_checker == 1):
                        utilities.check_for_tilda(tilda_before)
                        token = '|'  # fix to unary minus (4.5 prec, only comes first or after '(' )
                        minus_before = True
                    else:
                        minus_before = False  ######## if - before operator doesnt work, delete this
                        token = '_'  # fix to unary minus (highest prec, after everything else, number or operator)
                        utilities.check_for_minus(minus_before)
                        minus_before = True  ####### continue for if doest work: change this to false
                else:
                    utilities.check_for_minus(minus_before)
                    minus_before = False
                    utilities.check_for_tilda(tilda_before)
                    tilda_before = True
                    minus_first_checker = 0
                # if a new operator with lower precedence is inserted, combine the previous expression
                while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token] and (op_queue[0] != '|' and token != '|'):
                    combine(op_queue, node_stack)
                last_unary_prefix_seen_stack.insert(0, token)
                open_paren_count_stack.insert(0, 0)
            # special case for postfix unary expressions
            elif token == '!' or token == '#':
                utilities.check_for_minus(minus_before)
                minus_before = False
                utilities.check_for_tilda(tilda_before)
                tilda_before = False
                # if a new operator with lower precedence is inserted, combine the previous expression
                while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
                    combine(op_queue, node_stack)
                node_stack.insert(0, node_stack[0].clone())
                op_queue.insert(0, token)
            else:  # binary operator
                utilities.check_for_minus(minus_before)
                if token == '-':  ########## if binary - doesnt work, turn all of the code to false
                    minus_before = True
                else:
                    minus_before = False
                utilities.check_for_tilda(tilda_before)
                # if a new operator with lower precedence is inserted, combine the previous expression
                tilda_before = False
                while len(op_queue) > 0 and prec[op_queue[0]] >= prec[token]:
                    combine(op_queue, node_stack)
                op_queue.insert(0, token)
                open_operand_count -= 1

        prev_token = token

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

    paren_count = 0

    if len(infix) < 1:
        raise ValueError("Empty expression is prohibited")

    token_list = utilities.strToList(infix)
    for token in range(len(token_list) - 1):
        if (not token_list[token].isdigit()) and (not utilities.is_float(token_list[token])) and (
        not token_list[token] in "()+*&^%$@/!~#-"):
            raise ValueError("only numbers and operators allowed")

        if token_list[token] in "(+*&^%$@/~" and token_list[token + 1] in "+*&^%$@/~" and (
                token_list[token] != '+' and token_list[token + 1] != '~'):
            raise ValueError(
                "No Consecutive operators of such kind allowed: " + token_list[token] + " " + token_list[token + 1])

    for token in range(len(token_list)):
        if token_list[token] == '(':
            paren_count += 1
        if token_list[token] == ')':
            paren_count -= 1
            if paren_count < 0:
                raise SyntaxError("Wrong parenthesis usage")

        if token_list[token] in "+*&^%$@/" and (token == 0 or token == len(token_list) - 1):
            raise ValueError("wrong use of binary operators")

        if (token_list[token] in '~-' and token == len(token_list) - 1) or (token_list[token] in '!#' and token == 0):
            raise ValueError("wrong use of unary operators")

    if paren_count != 0:
        raise SyntaxError("Wrong parenthesis usage")


exp = "((2+--3!)+10)#"
exp = utilities.cleanExpression(exp)
expresssionErrors(exp)
ans = constructTreeFromInfix(exp)
print(evaluate(ans))
