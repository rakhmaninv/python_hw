import json
import os.path


def to_json(path):
    def decorator_json(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) is dict:
                # преобразование значений в строку т.к. комплексные числа не сериализуются в json
                result = {key: str(value) for key, value in result.items()}
            else:
                result = {' '.join(map(str, args)): str(result)}

            with open(f'{path}.json', 'w+', encoding='utf-8') as file:
                # если json файл пустой, создаем пустой список
                if os.stat(f'{path}.json').st_size == 0:
                    content = {}
                # иначе загружаем данные из файла
                else:
                    content = json.load(file)
                # добавляем в список и записываем в файл
                content.update(result)
                json.dump(content, file, indent=2)

            return result

        return wrapper

    return decorator_json
