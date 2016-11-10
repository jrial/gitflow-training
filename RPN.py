OPERATORS = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__div__,
}


class RPN(object):
    def __init__(self, expression):
        super(self.__class__, self).__init__()
        self._expression = expression

    def calculate(self):
        stack = []
        for elem in self._expression.split():
            try:
                stack.append(float(elem))
            except ValueError:
                try:
                    operator = OPERATORS.get(elem)
                    term2 = stack.pop()
                    term1 = stack.pop()
                    result = operator(term1, term2)
                    stack.append(result)
                except IndexError:
                    print("Malformed expression: {}".format(self._expression))
                    return
                except TypeError:
                    print("{} is not a valid operator!\nPossible values: {}".format(elem, ', '.join(OPERATORS)))
                    return
        print("\n>> {}\n".format(stack[0]))

    def print_expression(self):
        print(self._expression)
