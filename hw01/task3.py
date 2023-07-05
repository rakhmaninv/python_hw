# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
# подсказывать «больше» или «меньше» после каждой попытки.
from random import randint, choice

low_bound = 0
high_bound = 1000
guesses = 10
game_mode = ''
out_of_guesses_message = ''

while game_mode not in ('1', '2'):
    game_mode = input('кто будет угадывать: ты(1) или я(2)  ')

match game_mode:
    case '1':
        out_of_guesses_message = 'ха! человек - пережиток прошлого'
        num = randint(low_bound, high_bound)
        user_guess = int(input(f'я загадал число от {low_bound} до {high_bound}  '))
        guesses -= 1
        while guesses > 0:
            if user_guess > num:
                user_guess = int(input('больше  '))
            elif user_guess < num:
                user_guess = int(input('меньше  '))
            else:
                print('хм... тебе просто повезло')
                break
            guesses -= 1

    case '2':
        controls = 'управление: больше - "G" меньше - "L" правильно - "Y"'
        input_error_responses = ('что-что?', 'ничего не понял', 'уже не помнишь управление?',
                                 'что-то не то ты пишешь', 'господи...')
        out_of_guesses_message = 'прости, со мной такое первый раз'

        print(controls)
        print(f'загадай число от {low_bound} до {high_bound}')
        while guesses > 0:
            mid = (low_bound + high_bound) // 2
            match input(f'твое число - {mid}?  ').upper():
                case 'L':
                    high_bound = mid - 1
                case 'G':
                    low_bound = mid + 1
                case 'Y':
                    print('склонись перед мощью моего интеллекта!')
                    break
                case _:
                    print(choice(input_error_responses))
                    print(controls)
                    guesses += 1
            guesses -= 1

if guesses == 0:
    print(out_of_guesses_message)
