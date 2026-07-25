# Программа ведет викторину со столицами стран и ведет подсчет правильных/неправильных ответов

import random


def main():
    country_dict = get_dict()
    play_quiz = get_play_quiz(country_dict)


def get_dict():
    country = {'США': 'Вашингтон', 'Бразилия': 'Бразилиа', 'Россия': 'Москва', 'Беларусь': 'Минск', 'Польша': 'Варшава',
               'Германия': 'Берлин', 'Голландия': 'Амстердам', 'Китай': 'Пекин', 'Украина': 'Киев', 'Литва': 'Вильнюс',
               'Латвия': 'Рига', 'Франция': 'Париж', 'Великобритания': 'Лондон', 'Япония': 'Токио', 'Испания': 'Мадрид',}
    return country


def get_play_quiz(country_dict):
    # Создаю список из названия стран
    country = list(country_dict.keys())

    # Копия словаря, он будет использоваться для контроля 
    # кол-ва стран и убирает вариант повтора стран в викторине
    remaining_countries = {k:v for k, v in country_dict.items()}
    
    # Необязательные словари, в них я добавляю верные и неверные ответы
    true_dict = {}
    false_dict = {}

    # Счетчики
    num_count = 0           # кол-во попыток
    true_count = 0          # кол-во верных ответов
    false_count = 0         # кол-во неверных

    print('Игра викторина, нужно назвать столицу стран, в конце узнаете кол-во верных/неверных ответов')

    again = 'д'
    while again.lower() == 'д' and remaining_countries:
        # Случайным образом выбирается название страны  
        # Этот блок кода нужен для упрощения написания кода в дальнейшем,
        # чтобы не дублировать длинные строки (Принцип KISS)
        country_name = random.choice(list(remaining_countries.keys()))          # Получаем рандомное имя страны, для этого создается список по ключам(названиям стран)
        correct_capital = remaining_countries[country_name]                     # Получаем верное значение для столицы, для этого по ключу получаем название
        num_count += 1
        
        print(f'{num_count}. {country_name}')
        choice = input(f'Столица: ').strip()

        # Поиск в словаре столицы через in
        if choice == correct_capital:
            true_dict[country_name] = choice
            true_count += 1
        else:
            false_dict[country_name] = choice
            false_count += 1

        # Удаляем страну из словаря, чтобы не было повторов
        del remaining_countries[country_name]
        
        # Проверка на наличие стран
        # Когда их не будет, игра закончится автоматически
        if not remaining_countries:
            print('Страны закончились!')
            break
        
        again = input('Желаете продолжить? (д/н) ')

    print()
    print(f'Верных ответов: {true_count}\n'
          f'Правильно названные столицы стран: ')
    for k, v in true_dict.items():
        print(f'{k} - {v}')

    print()
    print(f'Неправильных ответов: {false_count}\n'
        f'Неправильно названные столицы стран (Ваш ответ/Верный ответ): ')
    for k, v in false_dict.items():
        print(f'{k} - {v}')

    print()
    print('Список стран и их столиц: ')
    for k, v in country_dict.items():
        print(f'{k} - {v}')

if __name__ == '__main__':
    main()