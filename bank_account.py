
class Account:
    def __init__(self):
        self.balance = 0.
        self.history = []

    def top_up(self):
        amount = float(input('На сколько пополнить счет? '))
        self.balance += amount

    def buy(self):
        cost = float(input('Сколько стоит покупка? '))
        if cost > self.balance:
            print(f'У вас на счету: {self.balance}. На покупку стоимостью {cost} не хватает средств.')
            return None
        name = input('Название покупки? ')
        self.balance -= cost
        self.history.append({'name': name, 'cost': cost})
        return None

    def print_history(self):
        if len(self.history) > 0:
            for item in self.history:
                print(item)
        else:
            print('История покупок пуста.')
        return None


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
            break
        else:
            print('Неверный пункт меню')
