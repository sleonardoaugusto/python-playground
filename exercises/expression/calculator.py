def calculate(expression):
    cleared_expr = clear(expression)
    n = None
    operator = None
    total = None
    for el in cleared_expr:
        if total is None:
            total = get_value(el)
        else:
            if el in ('+', '-'):
                operator = el
            else:
                n = get_value(el)
            if n and operator:
                if operator == '-':
                    total -= n
                else:
                    total += n
                n = None
                operator = None
    return total


def clear(expression):
    return expression.replace('(', '').replace(')', '')


def get_value(value):
    if value == 'x':
        return 3
    return int(value)
