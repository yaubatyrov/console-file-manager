import math


def test_filter():
    def func(x):
        return (x % 2) == 0

    lst = [1, 2, 3, 4, 5, 6]

    assert list(filter(func, lst)) == [2, 4, 6]


def test_filter_2():
    def func(x):
        return len(x) > 1

    lst = ['q', 'we', 'wer', 'r']

    assert list(filter(func, lst)) == ['we', 'wer']


def test_map():
    def func(x):
        return x ** 2

    lst = [1, 2, 3, 4]

    assert list(map(func, lst)) == [1, 4, 9, 16]


def test_map_2():
    def func(x):
        return x[0]

    lst = ['qwe', 'asd', 'zxc']

    assert list(map(func, lst)) == ['q', 'a', 'z']


def test_sorted():
    lst = [1, 9, 4, 5, 2]
    assert sorted(lst) == [1, 2, 4, 5, 9]


def test_sorted_2():
    lst = ['qwe', 'asd', 'zxc']
    assert sorted(lst) == ['asd', 'qwe', 'zxc']


def test_math_pi():
    assert 3. < math.pi < 4.


def test_math_sqrt():
    assert math.sqrt(256.) == 16.


def test_math_sqrt_2():
    assert math.sqrt(196.) == 14.


def test_math_pow():
    assert math.pow(3, 3) == 27


def test_math_pow_2():
    assert math.pow(2, 10) == 1024


def test_math_hypot():
    assert math.hypot(3, 4) == 5

