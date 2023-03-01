from random import choice

NUMBER = 8


def eight_queens():
    coord_x = []
    coord_y = []
    for i in range(NUMBER):
        x, y = [int(num) for num in input("Enter coordinates: ").split()]
        coord_x.append(x)
        coord_y.append(y)

    for i in range(NUMBER):
        for j in range(i + 1, NUMBER):
            if coord_x[i] == coord_x[j] or coord_y[i] == coord_y[j] or abs(coord_x[i] - coord_x[j]) == abs(
                    coord_y[i] - coord_y[j]):
                return False

    return True


# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше.


RAND_NUMBER = 9


def eight_queens_rand():
    coord_x = []
    coord_y = []

    for i in range(NUMBER):
        x = choice([i for i in range(RAND_NUMBER)])
        y = choice([i for i in range(RAND_NUMBER)])
        coord_x.append(x)
        coord_y.append(y)

    for i in range(NUMBER):
        for j in range(i + 1, NUMBER):
            if coord_x[i] == coord_x[j] or coord_y[i] == coord_y[j] or abs(coord_x[i] - coord_x[j]) == abs(
                    coord_y[i] - coord_y[j]):
                return False

    return True
