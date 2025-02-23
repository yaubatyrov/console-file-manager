import os
import shutil
import platform

from bank_account import run_bank_account
from quiz import play_quiz


def create_folder(name=None):
    if name is None:
        name = input("Введите название папки: ")
    try:
        os.makedirs(name, exist_ok=True)
    except Exception as e:
        print(f'Не удалось создать папку "{name}" в текущей рабочей директории. Детали: {e}')
        return
    print(f"Папка '{name}' создана.")


def delete_file_or_folder():
    name = input("Введите название файла или папки для удаления: ")
    if os.path.isdir(name):
        try:
            shutil.rmtree(name)
        except Exception as e:
            print(f'Не удалось удалить папку "{name}" в текущей рабочей директории. Детали: {e}')
            return
        print(f"Папка '{name}' удалена.")
    elif os.path.isfile(name):
        try:
            os.remove(name)
        except Exception as e:
            print(f'Не удалось удалить файл "{name}" в текущей рабочей директории. Детали: {e}')
            return
        print(f"Файл '{name}' удален.")
    else:
        print("Файл или папка не найдены.")


def copy_file_or_folder():
    source = input("Введите название копируемого файла или папки: ")
    destination = input("Введите новое имя файла или папки: ")
    if os.path.isdir(source):
        try:
            shutil.copytree(source, destination)
        except Exception as e:
            print(f'Не удалось скопировать папку "{source}" в расположение "{destination}". Детали: {e}')
            return
        print(f"Папка '{source}' скопирована в '{destination}'.")
    elif os.path.isfile(source):
        try:
            shutil.copy2(source, destination)
        except Exception as e:
            print(f'Не удалось скопировать файл "{source}" в расположение "{destination}". Детали: {e}')
            return
        print(f"Файл '{source}' скопирован в '{destination}'.")
    else:
        print("Файл или папка не найдены.")


def list_directory():
    print("Содержимое рабочей директории:")
    [print(item) for item in os.listdir()]


def list_directory_to_file():
    print("Сохраняем содержимое рабочей директории в файл...")
    folders = (x for x in os.listdir() if os.path.isdir(x))
    files = (x for x in os.listdir() if os.path.isfile(x))
    try:
        with open('listdir.txt', 'w') as f:
            f.write('folders: ' + str(folders) + '\n')
            f.write('files: ' + str(files) + '\n')
    except PermissionError:
        print("Ошибка: нет прав на запись в текущую директорию.")
    except Exception as e:
        print(f"Не удалось сохранить содержимое рабочей директории в файл. Ошибка: {e}")


def list_folders():
    print("Папки в рабочей директории:")
    [print(item) for item in os.listdir() if os.path.isdir(item)]


def list_files():
    print("Файлы в рабочей директории:")
    [print(item) for item in os.listdir() if os.path.isfile(item)]


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
        print("5 - Сохранить содержимое рабочей директории в файл")
        print("6 - Посмотреть только папки")
        print("7 - Посмотреть только файлы")
        print("8 - Просмотр информации об операционной системе")
        print("9 - Создатель программы")
        print("10 - Играть в викторину")
        print("11 - Мой банковский счет")
        print("12 - Смена рабочей директории")
        print("13 - Выход")

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
            list_directory_to_file()
        elif choice == "6":
            list_folders()
        elif choice == "7":
            list_files()
        elif choice == "8":
            print_os_info()
        elif choice == "9":
            print(author_info())
        elif choice == "10":
            play_quiz()
        elif choice == "11":
            run_bank_account()
        elif choice == "12":
            change_directory()
        elif choice == "13":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
