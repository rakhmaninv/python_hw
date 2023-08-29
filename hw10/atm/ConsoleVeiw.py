

class ConsoleView:

    def __init__(self, divisor):
        self.divisor = divisor

    def print_menu(self, balance) -> None:
        print('=' * 60)
        print(f'Баланс: {balance}')
        print('-' * 60)
        print('1 - Пополнить баланс\n'
              '2 - Снять наличные\n'
              '3 - Выйти'
              )
        print('=' * 60)

    def user_number_input(self, msg : str) -> int:
        user_input = input(msg)
        if not user_input.isdigit():
            if user_input[1:].isdigit() and user_input.startswith('-'):
                raise ValueError('Ошибка ввода: Введено отрицательное число')
            raise ValueError('Ошибка ввода: Введено не число.')
        if not input_validation(int(user_input)):
            raise ValueError(f'Ошибка ввода: Число должно быть кратно {INPUT_DIVISIBLE}.')
        return int(user_input)


if __name__ == '__main__':
    print('test')
