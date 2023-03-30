import argparse
import logging

FORMAT = '{asctime} {levelname} {funcName}-> {lineno}:{msg}'
logging.basicConfig(level=logging.INFO, filename='events.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def quadratic_equation(a: int | float, b: int | float, c: int | float) -> (str, float):
    """
    The function of calculating the roots of a quadratic equation with recording the results in a log.
    :param: 2
    :param: 6
    :param: -3
    :return: (-3.4364916731037085, 0.4364916731037085)
    """
    discriminant = b ** 2 - (4 * a * c)
    if discriminant < 0:
        logger.info(f'The roots of the quadratic equation are not obtained ')
        return f'No roots'
    elif discriminant == 0:
        try:
            x = (-b) / 2 * a
        except ZeroDivisionError as e:
            logger.error(f'Error dividing number {-b} by number {a}')
            return float('inf')
        logger.info(f'One root of the quadratic equation obtained - ({x})')
        return x
    else:
        try:
            x1 = (-b - (discriminant ** 0.5)) / (2 * a)
            x2 = (-b + (discriminant ** 0.5)) / (2 * a)
        except ZeroDivisionError as e:
            logger.error(f'Error: {e} -> dividing number {-b - (discriminant ** 0.5)} by number {a}')
            return float('inf')
        logger.info(f'Two roots of the quadratic equation are obtained ({x1}, {x2})')
        return x1, x2


def my_parser():
    """Parser function for entering arguments from the command line."""
    parser = argparse.ArgumentParser(description='We introduce the coefficients a, b and the free term c '
                                                 'to solve the quadratic equation')
    parser.add_argument('-a')
    parser.add_argument('-b')
    parser.add_argument('-c')
    args = parser.parse_args()
    return quadratic_equation(float(args.a), float(args.b), float(args.c))


if __name__ == "__main__":
    my_parser()
