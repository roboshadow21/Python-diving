class TriangleException(Exception):

    """Class - inherited from the base class Exception."""
    pass


class NotNegativeException(TriangleException):

    """The class throws an exception if the side of the triangle is a negative number."""

    def __init__(self, side):
        self.side = side

    def __str__(self):
        text = "below zero"
        if self.side < 0:
            return f"Side of triangle a with size {self.side} cannot be {text}"


class NotTriangleException(TriangleException):

    """The class throws an exception if the sum of any two sides of a triangle is less than the third."""

    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def __str__(self):
        return f"There is no triangle with sides {self.side_a} : {self.side_b} : {self.side_c}"