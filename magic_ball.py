import random

answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено',
           'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',
           'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',
           'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да',
           'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?')
print(f'Привет, {name}')


def magic_ball():
    while True:
        question = input('О чем ты хочешь узнать?')
        random_answer = random.choice(answers)
        print(random_answer)
        break


while True:
    magic_ball()
    again = input('Хочешь узнать еще о чем-то? да/нет ').lower().strip()  # Приводим строку к нижнему регистру
    if again != 'да':
        print('Возвращайся, если возникнут вопросы!')
        break
