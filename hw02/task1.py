# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def dec_to_hex(num: int) -> str:
    symbols = '0123456789abcdef'
    result = str()
    while num > 0:
        # вроде такой способ должен работать быстрее, чем +
        result = ''.join((symbols[num % 16], result))
        num //= 16
    return result


dec = int(input('число: '))
my_hex = dec_to_hex(dec)
if hex(dec)[2:] == my_hex:
    print(my_hex)
else:
    print(f'ошибка: {hex(dec)[2:]} != {my_hex}')
