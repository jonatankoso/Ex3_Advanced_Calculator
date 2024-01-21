import Tree
import utilities


def activate_calc(exp: str):
    """
    Function runs the functions pre-run of the calculator
    :param exp: expression to be calculated
    :return: none
    """
    exp = utilities.clean_expression(exp)
    Tree.expression_errors(exp)
    ans = Tree.construct_tree_from_infix(exp)
    return ans


def main_func():
    """
    Function runs the user interface and the calculation function
    :return: none
    """
    print("Welcome to Jonathan's calculator!")
    try:
        while True:
            try:
                exp = input("\nEnter your expression: ")
                print(Tree.evaluate(activate_calc(exp)))
            except (ValueError, TypeError, SyntaxError, ZeroDivisionError, OverflowError) as er:
                if isinstance(er, OverflowError):
                    print("Number too big")
                else:
                    print(er)
    except (KeyboardInterrupt, EOFError):
        print("\nClosed calculator")


if __name__ == '__main__':
    main_func()
