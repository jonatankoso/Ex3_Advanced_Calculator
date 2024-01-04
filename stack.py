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