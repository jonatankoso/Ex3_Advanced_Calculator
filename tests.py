import pytest
from main_prog import activate_calc
import Tree


@pytest.mark.parametrize("expression, outcome", [
        ("!3-3", "wrong use of unary operators"),
        ("3^*2", "No Consecutive operators of such kind allowed: ^ *"),
        ("3&&4", "No Consecutive operators of such kind allowed: & &"),
        (".5*7", "wrong representation of float number"),
        ("~~3", "tilda cannot come before an expression"),

        ("omega43o", "only numbers and operators allowed"),
        ("", "Empty expression is prohibited"),

        (" ", "Empty expression is prohibited"),
        (" \t", "Empty expression is prohibited"),

        ("~-3", 3),
        ("--2/3", 0.6666666666666666),
        ("4^3", 64),
        ("1.23#", 6),
        ("3!!", 720),
        ("(7$20)@15", 17.5),
        ("43 & 12 * 2", 24),
        ("15%4-1", 2),
        ("15%-6", -3),
        ("(-3-(-(-3)))", -6),
        ("~(5*2+~(3!))", -4),
        ("34@924##", 20),
        ("0^-1", "0 can only be brought by positive power"),
        ("-----2^-4", 0.0625),
        ("34&12$100/20", 5),

        ("34# *3 +4!-(-7--- --9)$ 123", -78),
        ("~-4.2^(2$6.7)+(3.1@1.5)/2-8^2 + 6.3", 14932.3666869907),
        ("7^2/4%3+65.4 * (---2.8 + (9.1 * 3.7)) - 1.5", 2066.398),
        ("~-6&2.33-(6+7&24/(3.1-9^2)) + 4.2 - 7.8 / 2.3 * 6.7", -22.101880337),
        ("(---5&2$3.4%2-----6^2+1@74! - 5.9)#", 85),
        ("(1234.5678# - - - 5) @ 51 & 101", 41),
        ("(2@5#-----(42+---4)) + 9.5 ^ 2@1", -5.219033485899999),
        ("(~(5*2+~(3!))) * 2$4! + -3-((-5))", -94),
        ("~-7+(3.2$4@(2^2)())-1+8/10+3 - 4.5", 9.3),
        ("((4!))# + 3% 6 +2@ 5^2&(10%5)/2", 9.5),
        ("~-8#-5.5+(((43))/(2))---6^2 ", -12),
        ("~-2$4.  5 $2 +(50@4 /3!!)%20", 4.5375),
        ("6& 2^3  ()()(())   $4+ 5          .5-9 /3", 18.5),
        (" 5 @ 4  % 3 . 2 + 1 - 6 / 3 - 2 . 1 - ~ 3", 1.2),
        ("~-(((((5&2$4)!#)%7 / 10 ) ^ 2 * 1000) % 3)!", 1),
        ("( ( ( (~-3!!^~-3!)#/5) ^ 100)#!#)", 61),
        ("2-(42^3!) & 0@2-(87  # #      !+30)", -749),
        ("-(--3 1-(582^3)+4@7    )-- -645", 197136686.5),
        ("2*92                  &(14%3     +(  51-10     )@7)", 52),
        ("(3847. 22 22 ## %7 ^- 2) ## ", 1)

    ])
def test_calc(expression, outcome):
    try:
        answer = Tree.evaluate(activate_calc(expression))
        assert answer == outcome
    except (ValueError, TypeError, SyntaxError, ZeroDivisionError, OverflowError) as er:
        assert str(er) == outcome
    except EOFError as exitErr:
        assert str(exitErr) == outcome
