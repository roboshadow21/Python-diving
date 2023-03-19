import pytest


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


def test_two_roots():
    assert quadratic_equation(1, 1, 0) == (-1.0, 0.0)


def test_no_roots():
    assert quadratic_equation(1, 1, 4) == 'No roots'


def test_one_root():
    assert quadratic_equation(0, 0, 1) == 0.0


if __name__ == '__main__':
    pytest.main(['-vv'])
