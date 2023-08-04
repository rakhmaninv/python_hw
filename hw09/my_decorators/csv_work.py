import csv


def to_csv(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(f'{path}.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(result)

        return wrapper

    return decorator


# def from_csv(path):
#     def decorator(func):
#         def wrapper():
#             with open(f'{path}.csv', 'r', newline='', encoding='utf-8') as file:
#                 values = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
#                 for row in values:
#                     func(*row)
#             # return func
#
#         return wrapper
#
#     return decorator

def from_csv(path):
    def decorator(func):
        result_dict = {}

        def wrapper():
            with open(f'{path}.csv', 'r', newline='', encoding='utf-8') as file:
                values = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
                for row in values:
                    result_dict[' '.join(map(str, row))] = func(*row)
            return result_dict

        return wrapper

    return decorator
