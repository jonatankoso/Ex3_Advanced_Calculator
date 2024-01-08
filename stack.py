class Stack:
    def __init__(self):
        '''
        Function initializes a stack object
        '''
        self.theStack = []

    def top(self):
        '''
        Function returns the highest item in the stack
        :return: top item in stack
        '''
        if self.is_empty():
            return "Empty Stack"
        else:
            return self.theStack[-1]

    def is_empty(self):
        '''
        Function checks if stack is empty
        :return: true if empty, false if not
        '''
        return len(self.theStack) == 0

    def push(self, item: str):
        '''
        Function inserts a new item to top of stack
        :param item: item to insert to stack
        :return: none
        '''
        self.theStack.append(item)

    def pop(self):
        '''
        Function return the top item of the stack and removes it from the stack
        :return: top item of stack
        '''
        if not self.is_empty():
            temp = self.theStack[-1]
            del (self.theStack[-1])
            return temp

        else:
            return "Empty Stack"


def prec(c):
    if c == '+' or c == '-':
        return 1
    elif c == '/' or c == '*':
        return 2
    elif c == '^':
        return 3
    elif c == '%':
        return 4
    elif c == '@' or c == '&' or c == '$':
        return 5
    elif c == '~' or c == '!':
        return 6
    else:
        return -1


def infix_to_postfix(s):
    post = []
    stack = []

    for i in range(len(s)):
        c = s[i]

        # If the encountered character is an operand, add it to the output string
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            post.append(c)
        # If the encountered character is an ‘(‘, push it to the stack
        elif c == '(':
            stack.append(c)
        # If the encountered character is an ‘)’, pop and add to the output string from the stack
        # until an ‘(‘ is encountered
        elif c == ')':
            while stack and stack[-1] != '(':
                post.append(stack.pop())
            stack.pop()  # Pop '('
        # If an operator is encountered
        else:
            while stack and (prec(s[i]) <= prec(stack[-1])):
                post.append(stack.pop())
            stack.append(c)

    # Pop all the remaining elements from the stack
    while stack:
        post.append(stack.pop())

    return ''.join(post)


# Driver code
exp = "5-3!"

# Function call
print(infix_to_postfix(exp))