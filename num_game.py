import random


def is_valid(n):
    """Проверяет, лежит ли число n в диапазоне от 1 до 100."""
    return 1 <= int(n) <= 100


def play_game():
    # Генерация нового случайного числа
    hidden_number = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку')

    count_attempt = 0
    while True:
        n = int(input("Введите число от 1 до 100: "))

        if not is_valid(n):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue  # Начинаем новый виток цикла без увеличения счетчика попыток

        count_attempt += 1

        if n < hidden_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > hidden_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == hidden_number:
            print('Вы угадали, поздравляем!')
            print(f'Было использовано {count_attempt} попыток')
            break  # Выходим из текущего цикла игры

    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


# Основной игровой цикл
while True:
    play_game()
    again = input('Сыграем еще раз? да/нет ').lower().strip()  # Приводим строку к нижнему регистру
    if again != 'да':
        print('До новых встреч!')
        break