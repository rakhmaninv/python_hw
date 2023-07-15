# Напишите программу банкомат.
#  Начальная сумма равна нулю +++
#  Допустимые действия: пополнить, снять, выйти +++
#  Сумма пополнения и снятия кратны 50 у.е.+++
#  Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. +++
#  После каждой третей операции пополнения или снятия начисляются проценты - 3% +++
#  Нельзя снять больше, чем на счёте +++
#  При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#  Любое действие выводит сумму денег +++
#  Дополнительно сохраняйте все операции поступления и снятия средств в список. +++

FEE_MIN = 30.00
FEE_MAX = 600.00
FEE_RATE = 0.015
INTEREST_RATE = 0.03
TAX_RATE = 0.1
INPUT_DIVISIBLE = 50
TAXABLE_MIN = 5_000_000

counter = 0
balance = 0
log = []
run = True


def logging(amount: int | float) -> None:
    global log
    log.append(amount)


def print_balance() -> None:
    global balance
    print(f'Баланс: {balance:_.2f}')


def print_menu() -> None:
    print('=' * 60)
    print_balance()
    print('-' * 60)
    print('1 - Пополнить баланс\n'
          '2 - Снять наличные\n'
          '3 - Выйти'
          )
    print('=' * 60)


def input_validation(user_input: int) -> bool:
    return user_input % INPUT_DIVISIBLE == 0


def user_number_input(msg: str) -> int:
    user_input = input(msg)
    if not user_input.isdigit():
        if user_input[1:].isdigit() and user_input.startswith('-'):
            raise ValueError('Ошибка ввода: Введено отрицательное число')
        raise ValueError('Ошибка ввода: Введено не число.')
    if not input_validation(int(user_input)):
        raise ValueError(f'Ошибка ввода: Число должно быть кратно {INPUT_DIVISIBLE}.')
    return int(user_input)


def deposit(amount: int) -> None:
    global balance
    balance += amount
    logging(amount)
    counter_check()
    print_balance()


def calculate_fee(amount: int) -> float:
    fee = amount * FEE_RATE
    if fee < FEE_MIN:
        return FEE_MIN
    elif fee > FEE_MAX:
        return FEE_MAX
    else:
        return fee


def withdraw(amount: int) -> None:
    global balance
    amount += calculate_fee(amount)
    if balance - amount < 0:
        raise ValueError(f'Сумма с комиссией({amount}) больше баланса.')
    balance -= amount
    logging(-amount)
    counter_check()
    print_balance()


def calculate_interest() -> int | float:
    global balance
    return balance * INTEREST_RATE


def deposit_interest() -> None:
    global balance
    interest = calculate_interest()
    balance += interest
    logging(interest)


def calculate_tax() -> int | float:
    global balance
    return balance * TAX_RATE


def charge_tax() -> None:
    global balance
    if balance > TAXABLE_MIN:
        tax = calculate_tax()
        balance -= tax
        logging(-tax)


def exit_atm() -> None:
    global run
    run = False
    print_balance()


def counter_check() -> None:
    global counter
    counter += 1
    if counter == 3:
        deposit_interest()
        counter = 0


while run:
    try:
        charge_tax()
        print_menu()
        match input('Выберете действие: '):
            case '1':
                deposit(user_number_input('Введите сумму для пополнения: '))
            case '2':
                withdraw(user_number_input('Введите сумму для снятия: '))
            case '3':
                exit_atm()
            case _:
                raise ValueError('Ошибка ввода: Такое действие не поддерживается.')

    except ValueError as e:
        print(e)

print(log)


