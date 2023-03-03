import csv
from random import choice
from my_decorators import decorator_data_to_json, decorator_data_from_csv


# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


def rand_numbers(rows: int, columns: int, nums_range: int) -> None:
    src_numbers = [i for i in range(nums_range)]

    with open('numbers.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in range(rows):
            numbers_lst = []
            for _ in range(columns):
                numbers_lst.append(choice(src_numbers))
            writer.writerow(numbers_lst)


@decorator_data_to_json
@decorator_data_from_csv
def quadratic_equation(a: int, b: int, c: int) -> (str, float):
    discriminant = b ** 2 - (4 * a * c)
    if discriminant < 0:
        return f'No roots'
    elif discriminant == 0:
        x = (-b) / 2 * a
        return x
    else:
        x1 = (-b - (discriminant ** 0.5)) / (2 * a)
        x2 = (-b + (discriminant ** 0.5)) / (2 * a)
        return x1, x2
