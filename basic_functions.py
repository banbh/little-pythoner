def is_empty(xx):
    assert type(xx) is list, "Argument to 'is_empty' was not a list"
    return len(xx) == 0

def head(xx):
    assert type(xx) is list, "Argument to 'head' was not a list"
    return xx[0]

def tail(xx):
    assert type(xx) is list, "Argument to 'tail' was not a list"
    assert len(xx) > 0, "List was empty"
    return xx[1:]

def cons(x, xx):
    assert type(xx) is list, "Second argument to 'cons' was not a list"
    return [x] + xx

def is_atom(x):
    return type(x) in [int, float, bool, str]

def is_seq(x, y):
    assert type(x) is str, 'First argument to is_equal was not a str'
    assert type(y) is str, 'Second argument to is_equal was not a str'
    return x == y

def add1(x):
    assert type(x) is int
    return x + 1

def sub1(x):
    assert type(x) is int
    assert x > 0
    return x - 1

def is_zero(x):
    assert type(x) is int
    return x == 0
