# Напишите функцию для транспонирования матрицы

MATRIX_LENGTH = 3
MATRIX_WIDTH = 3


def create_matrix(num1: int, num2: int) -> list[[int]]:
    matrix = [[i + 1 for i in range(num1)] for _ in range(num2)]
    return matrix


matr = create_matrix(MATRIX_LENGTH, MATRIX_WIDTH)

for i in matr:
    print(*i)


def transposed_matrix(matrix: list[[int]]) -> list[[int]]:
    res_matrix = list(zip(*matrix))
    return res_matrix


print()

transposed = transposed_matrix(matr)

for i in transposed:
    print(*i)

