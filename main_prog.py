import Tree
import utilities


def activate_calc(exp: str):
    exp = utilities.clean_expression(exp)
    Tree.expression_errors(exp)
    ans = Tree.construct_tree_from_infix(exp)
    print(Tree.evaluate(ans))


def main_func():
    print("Welcome to Jonathan's calculator!")
    try:
        while True:
            try:
                exp = input("\nEnter your expression: ")
                activate_calc(exp)
            except (ValueError, TypeError, SyntaxError, ZeroDivisionError, OverflowError) as er:
                if isinstance(er, OverflowError):
                    print("Number too big")
                else:
                    print(er)
    except (KeyboardInterrupt, EOFError):
        print("\nClosed calculator")


if __name__ == '__main__':
    main_func()
