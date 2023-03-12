from my_exceptions import NotNegativeException, NotTriangleException


class Triangle:
    """The class in which a triangle is created with sides a, b, c."""

    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        if a < 0:
            raise NotNegativeException(self.side_a)
        elif b < 0:
            raise NotNegativeException(self.side_b)
        elif c < 0:
            raise NotNegativeException(self.side_c)
        if self.side_a + self.side_b < self.side_c or self.side_a + self.side_c < self.side_b or \
                self.side_b + self.side_c < self.side_a:
            raise NotTriangleException(self.side_a, self.side_b, self.side_c)

    def __repr__(self):
        return f"Triangle({self.side_a}, {self.side_b}, {self.side_c})"


if __name__ == '__main__':
    triangle = Triangle(3, -2, 3)
    print(triangle)
    print(triangle.side_a, triangle.side_b, triangle.side_c)
