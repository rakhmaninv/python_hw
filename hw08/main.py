# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий
import csv
import json
import os
import pickle
from itertools import chain


def get_size(path) -> int:

    if os.path.isdir(path):
        total = 0
        for dir_path, folders, filenames in os.walk(path):
            for filename in filenames:
                total += os.path.getsize(os.path.join(dir_path, filename))

        return total
    else:
        return os.path.getsize(path)


def dir_info(start_dir: str, info: list[dict] = None) -> list[dict]:

    if info is None:
        info = []

    for dir_path, folders, filenames in os.walk(start_dir):
        for item in chain(folders, filenames):
            item_path = os.path.join(dir_path, item)
            info_dict = {'name': item,
                         'path': dir_path,
                         'size': get_size(item_path),
                         'type': 'directory' if os.path.isdir(item_path) else 'file',
                         }
            info.append(info_dict)
    return info


res = dir_info('..')

with(
    open('info.json', 'w', encoding='utf-8') as j,
    open('info.csv', 'w', newline='', encoding='utf-8') as c,
    open('info.pickle', 'wb') as p
):
    json.dump(res, j, indent=2)
    pickle.dump(res, p)
    writer = csv.DictWriter(c, fieldnames=res[0])
    writer.writeheader()
    writer.writerows(res)


# def test():
#     for dirpath, folders, filenames in os.walk('..'):
#         for item in *folders, *filenames:
#             print(os.path.join(dirpath, item))
#         # for file in filenames:
#         #     size = os.path.getsize(os.path.join(dirpath, file))
#         #     print(f'{dirpath}{file} - {size}')
#         # print(f'{dirpath =}\n{folders =}\n{filenames}')
#         # print('=' * 20)
#
#
# test()
