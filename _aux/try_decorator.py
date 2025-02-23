

def add_stars(print_func, *args):
    print('*' * 10)
    result = print_func(*args)
    print('-' * 10)
    return result


def add_stars_dec(print_func):
    def inner(*args):
        print('*' * 10)
        result = print_func(*args)
        print('-' * 10)
        return result
    return inner


@add_stars_dec
def say_hello(name):
    s = f'hello, {name}'
    print(s)
    return s


@add_stars_dec
def say_goodbye(name):
    s = f'goodbye, {name}'
    print(s)
    return s


def main():
    name = 'Ramil'
    # add_stars(say_hello, name)
    # add_stars(say_goodbye, name)
    # add_stars_dec(say_hello)(name)
    # add_stars_dec(say_hello)(name)
    res_1 = say_hello(name)
    res_2 = say_goodbye(name)
    print('Результаты:', res_1, res_2)


if __name__ == '__main__':
    main()
