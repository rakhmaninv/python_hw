# Создайте функцию генератор чисел Фибоначчи


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


it = iter(fibonacci())
for _ in range(51):
    print(next(it))

