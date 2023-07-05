# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: «Число является простым, если делится нацело только на единицу и на себя». Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.


LOW_BOUND = 0
HIGH_BOUND = 100000


while True:
    try:
        num = int(input(f'введите число от {LOW_BOUND} до {HIGH_BOUND}: '))
        if LOW_BOUND <= num <= HIGH_BOUND:
            break
        print("ввели неправильное число")
    except ValueError:
        print('ввели не число')

prime = True

if num > 1:
    for i in range(2, num // 2):
        if num % i == 0:
            prime = False
            break

    if prime is True:
        print(f'{num} - простое число')
    else:
        print(f'{num} - составное число')
else:
    print(f'{num} - не является ни простым, ни составным числом')
