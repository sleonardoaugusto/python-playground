from exercises.expression.calculator import calculate


def test_clear_expression():
    expression = '1+2+3'
    assert calculate(expression) == 6


def test_expression_with_x():
    expression = '1+2+x'
    assert calculate(expression) == 6


def test_expression_with_parenthesis():
    expression = '1+(2+x)'
    assert calculate(expression) == 6
