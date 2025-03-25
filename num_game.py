import random
hidden_number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
def is_valid(n):
    if 1 <= int(n) <= 100:
        return True
    else:
        return False
Flag = True
count_attempt = 0
while Flag:
    n = int(input("Введите число от 1 до 100: "))
    if not is_valid(n):
        print("А может быть все-таки введем целое число от 1 до 100?")
        count_attempt += 1
    elif n < hidden_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count_attempt += 1
    elif n > hidden_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count_attempt += 1
    elif n == hidden_number:
        print('Вы угадали, поздравляем!')
        print(f'Было использовано {count_attempt} попыток')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        again = input('Сыграем еще раз? да/нет ')
        Flag = False

print(is_valid(n))
