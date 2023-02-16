import os


# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

path = r"C:\User\Docs\my_file.txt"


def path_to_file(url: str) -> tuple:
    path_abs = os.path.split(os.path.abspath(url))

    file_name = path_abs[1].split(".")

    result = path_abs[0], file_name[0], file_name[1]
    return result
