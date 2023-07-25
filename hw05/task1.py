# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def path_parse(path_string: str) -> tuple[str]:
    *path, name = path_string.split('\\')
    *name, ext = name.split('.')
    path = '\\'.join(path)
    name = '.'.join(name)

    return path, name, ext


test_str = 'C:\\Users\\user\\Documents\\gb\\python_spec\\hw\\hw05\\task1.py'
print(path_parse(test_str))
