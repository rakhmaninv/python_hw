# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
from itertools import combinations

MAX_WEIGHT = 12


def fill_backpack_easy(bp: list, max_weight: int, stuff: dict):
    current_weight = 0
    for k, v in stuff.items():
        if k not in bp and current_weight + v <= max_weight:
            bp.append(k)
            current_weight += v


def fill_backpack_hard(max_weight: int, stuff: dict):
    # Задание немного не понял. Если нужно только с максимальной загрузкой выводить, то все правильно.
    # А если вообще все которые не превышают, то на 22 строке sum(comb[1]) == max_weight заменить на <=
    for i in range(len(stuff) + 1):
        for comb in combinations(stuff.items(), i):
            comb = list(zip(*comb))
            if comb and sum(comb[1]) == max_weight:
                print(f'{", ".join(comb[0])}:  weight:{sum(comb[1])}')


backpack = []
camping_items = {
    'sleeping bag': 5,
    'axe': 3,
    'pot': 4,
    'cup': 1,
    'flashlight': 2,
    'rope': 1,
    'knife': 2,
    'tent': 5,
}
fill_backpack_easy(backpack, MAX_WEIGHT, camping_items)
print(', '.join(backpack))
print('=' * 50)
fill_backpack_hard(MAX_WEIGHT, camping_items)
