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
