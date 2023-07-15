# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где
# ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def kwargs_to_dict(**kwargs) -> dict[str, str]:
    result = {}
    for k, v in kwargs.items():
        if v.__hash__:
            result.setdefault(v, k)
        else:
            result.setdefault(str(v), k)
    # Однострочники: return {v if v.__hash__ else str(v): k for k, v in kwargs.items()}
    # по  условию не совсем подходит но зато гораздо проще: return {str(v): k for k, v in kwargs.items()}
    return result


test_dict = kwargs_to_dict(t_str='qwe',
                           t_int=10,
                           t_float=123.45,
                           t_list=[1, 2, 3],
                           t_dict={1: 'one', 2: 'two'},
                           t_set={1, 1, 2, 3},
                           )
print(test_dict)
