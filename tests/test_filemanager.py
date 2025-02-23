import os
from main import (create_folder, delete_file_or_folder,
                  copy_file_or_folder, list_directory,
                  list_folders, list_files, get_os_info, author_info,
                  change_directory)

from quiz import check_celebrity_date
from bank_account import Account


# Викторина

def test_check_celebrity_date_1():
    assert check_celebrity_date('А.С.Пушкин', year=1799) is True


def test_check_celebrity_date_2():
    assert check_celebrity_date('А.С.Пушкин', year=1800) is False


def test_check_celebrity_date_3():
    assert check_celebrity_date('А.С.Пушкин', day=6) is True


def test_check_celebrity_date_4():
    assert check_celebrity_date('А.С.Пушкин', day='kk') is False


# Файловый менеджер


def test_os_info():
    system, release = get_os_info()
    assert system == 'Windows'


def test_author_info():
    assert author_info() == "Создатель программы: Рамиль Яубатыров"


def test_create_folder():
    cwd = os.getcwd()
    folder_name = 'folder_0'
    counter = 1
    while folder_name in os.listdir(cwd):
        folder_name = f'folder_{counter}'
        counter += 1

    full_path = os.path.join(cwd, folder_name)

    create_folder(folder_name)
    assert os.path.isdir(full_path)


# Банковский счет


def test_account_top_up():
    account = Account(new=True)
    assert account.get_balance() == 0
    account.top_up(5)
    assert account.get_balance() == 5


def test_buy():
    account = Account(new=True)
    account.top_up(5)
    assert account.get_balance() == 5
    account.buy(3, 'паровозик')
    assert account.get_balance() == 2
    assert account.get_history()[-1]['name'] == 'паровозик'


def test_account_save_to_file():
    account = Account(new=True)
    assert account.get_balance() == 0
    account.top_up(5)
    assert account.get_balance() == 5
    account.save_to_file()

    account_2 = Account(new=False)
    assert account_2.get_balance() == 5
