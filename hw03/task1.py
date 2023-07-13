# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей


def get_unique_items(dict_of_tuples: dict) -> set:
    unique_items = set()

    for k, v in dict_of_tuples.items():
        temp_set = set.union(*[set(v2) for k2, v2 in dict_of_tuples.items() if k2 != k])
        unique_items = unique_items | (set(v) - temp_set)

    return unique_items


def all_but_one(dict_of_tuples: dict) -> dict:
    result = {}
    for k, v in dict_of_tuples.items():
        temp_set = set.intersection(*[set(v2) for k2, v2 in dict_of_tuples.items() if k2 != k])
        temp_set -= set(v)
        if temp_set:
            result[k] = tuple(temp_set)

    return result


campers = {
    'first': ('sleeping bag', 'axe', 'pot', 'cup', 'flashlight', 'rope'),
    'second': ('cup', 'sleeping bag', 'first-aid kit', 'knife', 'pan'),
    'third': ('sleeping bag', 'cup', 'knife', 'tent', 'flashlight', 'pot'),
}

print(f'all have: {", ".join(set.intersection(*list(map(set, campers.values()))))}')
print(f'unique items: {", ".join(get_unique_items(campers))}')
for k, v in all_but_one(campers).items():
    for i in v:
        print(f'all but {k} have {i}')
