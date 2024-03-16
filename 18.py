import re

class Operator:
    def __init__(self, symbol, precedence, left_associativity):
        self.symbol = symbol
        self.precedence = precedence
        self.left_associativity = left_associativity

operators = {
    "||": Operator("||", 1, True),
    "&&": Operator("&&", 2, True),
    "|": Operator("|", 3, True),    
    "^": Operator("^", 5, True),
    "&": Operator("&", 5, True),    
    "==": Operator("==", 6, True),
    "!=": Operator("!=", 6, True),   
    "<<": Operator("<<", 7, True),
    ">>": Operator(">>", 7, True),
    "<": Operator("<", 8, True),
    "<=": Operator("<=", 8, True),
    ">": Operator(">", 8, True),
    ">=": Operator(">=", 8, True),
    "<<": Operator("<<", 9, True),
    ">>": Operator(">>", 9, True),
    "+": Operator("+", 10, True),
    "-": Operator("-", 10, True),
    "*": Operator("*", 11, True),
    "/": Operator("/", 11, True),
    "%": Operator("%", 11, True),
    "!": Operator("!", 12, False),
    "~": Operator("~", 12, False),
}

def infix_to_rpn(input_exp):
    stack = []
    output_exp = []

    symbols = re.findall(r"\d+|\S", input_exp)

    for symbol in symbols:
        if symbol.isdigit():
            output_exp.append(symbol)
        elif symbol == "(":
            stack.append(symbol)
        elif symbol == ")":
            while stack and stack[-1] != "(":
                output_exp.append(stack.pop())
            stack.pop()
        elif symbol in operators:
            operator = operators[symbol]
            while stack and stack[-1] in operators and \
                    ((operator.left_associativity and operator.precedence <= operators[stack[-1]].precedence)):
                output_exp.append(stack.pop())
            stack.append(symbol)
        else:
            raise ValueError("Невалидный символ: {}".format(symbol))

    while stack:
        output_exp.append(stack.pop())

    return " ".join(output_exp)

def tests():
    assert infix_to_rpn("1 - 5 * 3") == "1 5 3 * -"
    assert infix_to_rpn("1 - (5 * 3)") == "1 5 3 * -"
    assert infix_to_rpn("1 * (5 - 3)") == "1 5 3 - *"
    assert infix_to_rpn("1 * (5 - 3) / 7") == "1 5 3 - * 7 /"
    assert infix_to_rpn("1 * ((5 + 3) / 7)") == "1 5 3 + 7 / *"
    assert infix_to_rpn("1 & (5 | 3)") == "1 5 3 | &"
    assert infix_to_rpn("!1 | (5 & 3)") == "1 ! 5 3 & |"
    
    print("Все тесты пройдены!")

tests()