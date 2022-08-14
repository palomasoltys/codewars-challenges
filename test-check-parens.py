from check_parens_stack import is_balanced


def test_balanced_with_letters():
    assert is_balanced("({a+b})") == True


def test_no_balanced_with_letters():
    assert is_balanced("))((a+b}{") == False


def test_no_balanced_no_letters():
    assert is_balanced("))") == False


def test_balanced_with_expressions():
    assert is_balanced("[a+b]*(x+2y)*{gg+kk}") == True
