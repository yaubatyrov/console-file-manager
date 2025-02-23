def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def operation(x, y, op):
    return add(x, y) if op == 'add' else mult(x, y)


if __name__ == '__main__':
    result = operation(3, 5, 'add')
    print(result)
