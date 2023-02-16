import os


# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

path = r"C:\User\Docs\my_file.txt"


def path_to_file(url: str) -> tuple:
    path_abs = os.path.split(os.path.abspath(url))

    file_name = path_abs[1].split(".")

    result = path_abs[0], file_name[0], file_name[1]
    return result

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


li1 = ["Bob", "John"]
li2 = [100, 300]
li3 = ["10.25%", "12%"]

result = {key: (value[i] * value[i + 1]) / 100 for key in li1 for value in
          list(zip(li2, [float(el[:-1]) for el in li3])) for i in
          range(len(li1) - 1)}