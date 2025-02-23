from _aux.try_ternary import add, mult, operation


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_mult():
    assert mult(2, 3) == 6
    assert mult(-1, 5) == -5
    assert mult(0, 10) == 0
    assert mult(2.5, 4) == 10.0


def test_operation_add():
    assert operation(3, 5, 'add') == 8
    assert operation(-2, -3, 'add') == -5


def test_operation_mult():
    assert operation(3, 5, 'mult') == 15
    assert operation(-2, -3, 'mult') == 6
