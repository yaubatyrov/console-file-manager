CELEBRITIES = {
    'А.С.Пушкин': '06.06.1799',
    'М.Ю.Лермонтов': '15.10.1814',
}


def play_quiz():

    celebrity = 'А.С.Пушкин'
    year = input(f'Введите год рождения {celebrity}: ')
    while not check_celebrity_date(celebrity, year=year):
        print("Не верно")
        year = input(f'Введите год рождения {celebrity}: ')

    day = input(f'Введите день рождения {celebrity}? ')
    while not check_celebrity_date(celebrity, day=day):
        print("Не верно")
        day = input(f'Введите день рождения {celebrity}? ')
    print('Верно')


def check_celebrity_date(celebrity, year=None, month=None, day=None):
    if celebrity not in CELEBRITIES:
        print(f'Знаменитость "{celebrity}" не найдена')
        return False

    date = CELEBRITIES[celebrity]
    real_day, real_month, real_year = (int(x) for x in date.split('.'))

    is_correct = True
    for user_date, real_date in [
        (year, real_year),
        (month, real_month),
        (day, real_day),
    ]:
        if user_date is None:
            continue

        try:
            user_date = int(user_date)
        except ValueError:
            print('Необходимо ввести число')
            return False

        if user_date != real_date:
            is_correct = False

    return is_correct


if __name__ == '__main__':
    play_quiz()
