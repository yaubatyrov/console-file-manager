import os
import shutil
import platform

from bank_account import run_bank_account
from quiz import play_quiz


def create_folder(name=None):
    if name is None:
        name = input("Введите название папки: ")
    os.makedirs(name, exist_ok=True)
    print(f"Папка '{name}' создана.")


def delete_file_or_folder():
    name = input("Введите название файла или папки для удаления: ")
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Папка '{name}' удалена.")
    elif os.path.isfile(name):
        os.remove(name)
        print(f"Файл '{name}' удален.")
    else:
        print("Файл или папка не найдены.")


def copy_file_or_folder():
    source = input("Введите название копируемого файла или папки: ")
    destination = input("Введите новое имя файла или папки: ")
    if os.path.isdir(source):
        shutil.copytree(source, destination)
        print(f"Папка '{source}' скопирована в '{destination}'.")
    elif os.path.isfile(source):
        shutil.copy2(source, destination)
        print(f"Файл '{source}' скопирован в '{destination}'.")
    else:
        print("Файл или папка не найдены.")


def list_directory():
    print("Содержимое рабочей директории:")
    for item in os.listdir():
        print(item)


def list_folders():
    print("Папки в рабочей директории:")
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)


def list_files():
    print("Файлы в рабочей директории:")
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)


def get_os_info():
    return platform.system(), platform.release()


def print_os_info():
    system, release = get_os_info()
    print("Информация об ОС:")
    print(system, release)


def author_info():
    return "Создатель программы: Рамиль Яубатыров"


def change_directory():
    path = input("Введите путь к новой рабочей директории: ")
    try:
        os.chdir(path)
        print(f"Рабочая директория изменена на {os.getcwd()}")
    except FileNotFoundError:
        print("Ошибка: Директория не найдена.")
    except NotADirectoryError:
        print("Ошибка: Указан путь к файлу, а не к папке.")
    except PermissionError:
        print("Ошибка: Недостаточно прав для смены директории.")


def main():
    while True:
        print("\nМеню:")
        print("1 - Создать папку")
        print("2 - Удалить (файл/папку)")
        print("3 - Копировать (файл/папку)")
        print("4 - Просмотр содержимого рабочей директории")
        print("5 - Посмотреть только папки")
        print("6 - Посмотреть только файлы")
        print("7 - Просмотр информации об операционной системе")
        print("8 - Создатель программы")
        print("9 - Играть в викторину")
        print("10 - Мой банковский счет")
        print("11 - Смена рабочей директории")
        print("12 - Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            create_folder()
        elif choice == "2":
            delete_file_or_folder()
        elif choice == "3":
            copy_file_or_folder()
        elif choice == "4":
            list_directory()
        elif choice == "5":
            list_folders()
        elif choice == "6":
            list_files()
        elif choice == "7":
            print_os_info()
        elif choice == "8":
            print(author_info())
        elif choice == "9":
            play_quiz()
        elif choice == "10":
            run_bank_account()
        elif choice == "11":
            change_directory()
        elif choice == "12":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
