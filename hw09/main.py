# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import cmath
import math
from random import uniform
from my_decorators import *

PATH = 'values'
REP = 200


@to_json(PATH)
@from_csv(PATH)
def quadratic_equation(a: int | float, b: int | float, c: int | float) -> tuple[float] | tuple[complex]:
    root_1 = None
    root_2 = None
    if a != 0:
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        elif discriminant == 0:
            root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        else:
            root_1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
            root_2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    else:
        if b != 0:
            root_1 = round(-c / b, 3)
        else:
            raise ValueError('Not valid equation')

    # return root_1 if root_2 is None else root_1, root_2
    return tuple(filter(None, (root_1, root_2)))


@to_csv(PATH)
@repeats(REP)
def generate_values(min_val, max_val):
    return [round(uniform(min_val, max_val), 3) for _ in range(3)]


if __name__ == '__main__':
    try:
        generate_values(-10, 10)
        quadratic_equation()


    except ValueError as e:
        print(e)
