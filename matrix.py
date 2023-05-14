from random import randint


class Matrix:
    """The class creates two-dimensional matrices and contains methods for mathematical operations with them."""

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = [[]]

    def create_matrix(self, low_border, upper_border):
        """The method generates a two-dimensional matrix, filling it with random numbers in a given range."""
        self.matrix = [[randint(low_border, upper_border) for _ in range(self.row)] for _ in range(self.column)]
        return self.matrix

    def show_matrix(self):
        """The method prints a representation of the two-dimensional matrix for the user."""
        for i in self.matrix:
            print(i)

    def __repr__(self):
        return f'matrix = Matrix({self.row}, {self.column})'

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        result_matrix = [[0 for _ in range(self.row)] for _ in range(self.column)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result_matrix

    def __mul__(self, other):
        result_matrix = [[0 for _ in range(self.row)] for _ in range(self.column)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                for k in range(len(self.matrix)):
                    result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result_matrix


if __name__ == '__main__':
    m1 = (Matrix(4, 4))
    m2 = (Matrix(4, 4))
    m3 = (Matrix(4, 4))

    m1.create_matrix(1, 5)
    m2.create_matrix(1, 5)

    m3.matrix = m1 + m2
    m1.show_matrix()
    print()
    m2.show_matrix()
    print()
    m3.show_matrix()

    m3.matrix = m1 * m2
    print()
    m3.show_matrix()
