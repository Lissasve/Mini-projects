import random

dgts = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambig_chars = 'il1Lo0O'  # неоднозначные символы


def generate_password(lenght, chars):
    return ''.join(random.choice(chars) for _ in range(lenght))  # генерируем один пароль


def questions():
    chars = []

    if content_of_numbers.lower() == 'да':
        chars.extend(dgts)  # добавляем в список
    if content_of_uppercase.lower() == 'да':  # добавляем в список
        chars.extend(uppercase_letters)  # добавляем в список
    if content_of_lowercase.lower() == 'да':  # добавляем в список
        chars.extend(lowercase_letters)  # добавляем в список
    if content_of_punctuation.lower() == 'да':  # добавляем в список
        chars.extend(punctuation)
    if not_content_ambig_chars.lower() == 'да':
        chars = [char for char in chars if char not in ambig_chars]  # удаляем из списка неоднозначные символы
    return chars


number_of_passwords = int(input('Введите количество паролей для генерации:'))  # количество паролей
lenght = int(input('Сколько символов должно быть в пароле?:'))  # длина пароля
content_of_numbers = input('Включать ли цифры от 0 до 9? да/нет:')  # включать ли цифры
content_of_uppercase = input('Включать ли прописные буквы? да/нет:')  # включать буквы в верхнем регистре
content_of_lowercase = input('Включать ли строчные буквы? да/нет:')  # включать буквы в нижнем регистре
content_of_punctuation = input('Включать ли символы пунктуации? да/нет:')  # включать символы пунктуации
not_content_ambig_chars = input('Исключать ли неоднозначные символы? да/нет:')  # исключить неоднозначные символы

chars = questions()  # формируем набор символов для пароля

for i in range(number_of_passwords):  # генерируем необходимое количество паролей
    password = generate_password(lenght, chars)
    print(f'Пароль {i + 1}: {password}')
