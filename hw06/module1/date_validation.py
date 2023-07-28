_END_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _is_leap(year) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def date_check(date: str) -> bool:
    day, month, year = tuple(map(int, date.split('.')))
    # проверка года
    if year not in range(1, 10000):
        return False
    # проверка месяца
    if month not in range(1, 13):
        return False
    # проверка дня
    if month == 2 and _is_leap(year):
        if day > _END_OF_MONTH[month - 1] + 1:
            return False
    else:
        if day > _END_OF_MONTH[month - 1]:
            return False

    return True



