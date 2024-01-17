import Tree
import utilities

def main_func():
    print("Welcome to Jonathan's calculator!")
    try:
        while True:
            try:
                exp = input("\nEnter your expression: ")
                exp = utilities.cleanExpression(exp)
                Tree.expresssionErrors(exp)
                ans = Tree.constructTreeFromInfix(exp)
                print(Tree.evaluate(ans))
            except (ValueError, TypeError, SyntaxError, ZeroDivisionError, OverflowError) as er:
                if isinstance(er, OverflowError):
                    print("Number too big")
                else:
                    print(er)
    except (KeyboardInterrupt, EOFError):
        print("\nClosed calculator")

if __name__ == '__main__':
    main_func()
