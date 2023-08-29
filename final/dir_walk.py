# ОПИСАНИЕ:
# программа получает на вход путь до директории и собирает информацию об объектах находящихся в ней.
# ИНСТРУКЦИЯ:
# 1. В терминале с помощью cd перейти в директорию с программой
# 2. Запустить программу с флагом -path и пути до нужной директории
#    Пример:> python .\dir_walk.py -path C:\Users\user\Documents\gb\python_spec\hw\
# 3. Создастся файл "files.log" в котором будет информация о файлах и директориях

# python .\dir_walk.py -path



import argparse
import os
from collections import namedtuple
import logging


parser = argparse.ArgumentParser(prog='Work with data')
parser.add_argument('-path', metavar='path', type=str, default=os.getcwd())

Obj = namedtuple('Obj', ['name', 'parent_folder', 'file_ext', 'flag_folder'], defaults=[None, 'FILE'])

logging.basicConfig(filename='files.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def directory_walk(path):
    data = []
    for line in os.walk(path):
        *parent_path, parent_folder = line[0].split("\\")
        for file in line[2]:
            file_name, extension = file, None
            if '.' in file:
                file_name, extension = file.rsplit('.', 1)
            o = Obj(file_name, parent_folder, extension)
            logger.info(f'{o.parent_folder} / {o.name}  {o.file_ext}  {o.flag_folder} ')
            data.append(o)
        for directory in line[1]:
            o = Obj(directory, parent_folder, flag_folder='FOLDER')
            logger.info(f'{o.parent_folder} / {o.name}  {o.file_ext}  {o.flag_folder} ')
            data.append(o)


if __name__ == '__main__':
    args = parser.parse_args()
    directory_walk(args.path)
