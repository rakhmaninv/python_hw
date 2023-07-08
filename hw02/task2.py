# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def my_gcd(fraction: list[int]) -> int:
    a = min(fraction)
    b = max(fraction)
    while b:
        a, b = b, a % b
    return abs(a)


def fraction_split(fraction: str) -> list[int]:
    return list(map(int, fraction.split('/')))


def fraction_operations(frac_1: list[int], frac_2: list[int], op: str) -> list[int]:
    match op:
        case '+':
            # a/b + c/d = (ad + cb)/bd
            result = list((frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1], frac_1[1] * frac_2[1]))
        case '*':
            # a/b * c/d = ac/bd
            result = list((frac_1[0] * frac_2[0], frac_1[1] * frac_2[1]))
        case _:
            raise ValueError('поддерживаемые операции с дробями: "+", "*"')

    gcd = my_gcd(result)
    for i in result:
        i /= gcd
    return result


def fraction_validation(fraction: list[int], validator) -> bool:
    temp = Fraction(fraction[0], fraction[1])
    return validator == temp


def fraction_input(msg: str) -> str:
    valid = False
    fraction = str()
    while not valid:
        try:
            allowed_symbols = {'/': 0, '-': 0}
            fraction = input(msg).replace(' ', '')
            str_len = len(fraction)

            for i in range(str_len):
                # проверяем встречаются ли допустимые символы больше 1 раза
                if fraction[i] in allowed_symbols:
                    allowed_symbols[fraction[i]] += 1
                    if allowed_symbols[fraction[i]] >= 2:
                        raise ValueError(f'допустим только по одному символу {allowed_symbols.keys()}')
                # проверяем есть ли недопустимые символы
                if not fraction[i].isdigit() and fraction[i] not in allowed_symbols.keys():
                    raise ValueError(f'допустимы только цифры и символы {", ".join(allowed_symbols.keys())}')

                if i == str_len - 1:
                    valid = True
        except ValueError as er:
            print(er)

    return fraction


first: list[int] = fraction_split(fraction_input('введи первую дробь вида "a/b": '))
second: list[int] = fraction_split(fraction_input('введи вторую дробь вида "a/b": '))

try:
    frac_sum: list[int] = fraction_operations(first, second, '+')
    frac_res: list[int] = fraction_operations(first, second, '*')

    sum_validator = Fraction(first[0], first[1]) + Fraction(second[0], second[1])
    res_validator = Fraction(first[0], first[1]) * Fraction(second[0], second[1])

    if fraction_validation(frac_sum, sum_validator):
        print(f'сумма: {frac_sum}')
    if fraction_validation(frac_res, res_validator):
        print(f'произведение: {frac_res}')
except ValueError as e:
    print(e)
