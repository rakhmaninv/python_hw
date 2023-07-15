# Напишите функцию для транспонирования матрицы
from copy import deepcopy


def matrix_transpose(matrix: list[list], *, copy=False) -> list[list] | None:
    if copy:
        new_matrix = deepcopy(matrix)
        return list(map(list, zip(*new_matrix)))
    else:
        matrix[:] = list(map(list, zip(*matrix)))


test1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
print(f'test 1: {test1}')
print(f'result: {matrix_transpose(test1, copy=True)}')
print(f'test 1: {test1}')
print('=' * 100)

test2 = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40]]
print(f'test 2: {test2}')
# None т.к. не возвращаем новый список, а изменяем передаваемый
print(f'result: {matrix_transpose(test2)}')
print(f'test 2: {test2}')
