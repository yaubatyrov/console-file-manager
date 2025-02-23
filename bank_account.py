import os
import json
import pickle


class Account:

    ACCOUNT_FILE_PICKLE = r'data/account_info.pickle'
    ACCOUNT_FILE_JSON = r'data/account_info.json'

    def __init__(self, new=False):
        self.file_format = 'json'
        self.balance = 0
        self.history = []
        if not new:
            self.read_from_file()

    def get_balance(self):
        return self.balance

    def top_up(self, amount=None):
        if amount is None:
            amount_str = input('На сколько пополнить счет? ')
            try:
                amount = float(amount_str)
            except ValueError:
                print('Не удалось пополнить счет. Для пополнения необходимо ввести число')
                return

        if amount <= 0:
            print('Ошибка: сумма пополнения должна быть положительной.')
            return

        self.balance += amount
        print(f'Счет пополнен на {amount}. Текущий баланс: {self.balance}')

    def buy(self, cost=None, name=None):
        if cost is None:
            try:
                cost = float(input('Сколько стоит покупка? '))
            except ValueError:
                print('Не удалось совершить покупку. Цена должна быть числом')
                return
        if cost > self.balance:
            print(f'У вас на счету: {self.balance}. На покупку стоимостью {cost} не хватает средств.')
            return None
        if name is None:
            name = input('Название покупки? ')
        self.balance -= cost
        self.history.append({'name': name, 'cost': cost})
        return None

    def get_history(self):
        return self.history

    def print_history(self):
        if len(self.history) > 0:
            [print(item) for item in self.history]
        else:
            print('История покупок пуста.')
        return None

    def read_from_file(self):
        return self.read_from_json() if self.file_format == 'json' else self.read_from_pickle()

    def read_from_pickle(self):
        if os.path.exists(self.ACCOUNT_FILE_PICKLE):
            with open(self.ACCOUNT_FILE_PICKLE, 'rb') as f:
                self.balance, self.history = pickle.load(f)

    def read_from_json(self):
        if os.path.exists(self.ACCOUNT_FILE_JSON):
            with open(self.ACCOUNT_FILE_JSON, 'r') as f:
                try:
                    data = json.load(f)
                except Exception as e:
                    print(f'Не удалось прочитать файл {self.ACCOUNT_FILE_JSON}, детали: {e}')
                else:
                    self.balance = data['balance']
                    self.history = data['history']

    def save_to_file(self):
        return self.save_to_json() if self.file_format == 'json' else self.save_to_pickle()

    def save_to_pickle(self):
        with open(self.ACCOUNT_FILE_PICKLE, 'wb') as f:
            pickle.dump((self.balance, self.history), f)

    def save_to_json(self):
        with open(self.ACCOUNT_FILE_JSON, 'w') as f:
            json.dump({'balance': self.balance, 'history': self.history}, f)


def run_bank_account():
    account = Account()
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            account.top_up()
        elif choice == '2':
            account.buy()
        elif choice == '3':
            account.print_history()
        elif choice == '4':
            account.save_to_file()
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    run_bank_account()
