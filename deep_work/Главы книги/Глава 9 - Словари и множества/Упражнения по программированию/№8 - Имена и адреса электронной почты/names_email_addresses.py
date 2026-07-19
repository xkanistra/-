# Программа позволяет взаимодействовать с ключ:значение в словаре и консервирует/расконсервирует из файла


import logging
import pickle

DATA_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№8 - Имена и адреса электронной почты/email.dat'

# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Настройка логгера, простая
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename='Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№8 - Имена и адреса электронной почты/app.log',
    filemode='a' 
)

def main():
    email_file = open_data()
    if not email_file:
        return

    # Создаем переменную для выбора пользователем
    choice = 0

    # Цикл для работы программы
    while choice != QUIT:
        # Запуск меню для выбора действия
        choice = get_menu_choice()

        # Обработка других вариантов действия
        if choice == LOOK_UP:
            look_up(email_file)
        elif choice == ADD:
            add(email_file)
        elif choice == CHANGE:
            change(email_file)
        elif choice == DELETE:
            delete(email_file)
        else:
            save_data(email_file) 
            break
         

def get_menu_choice():
    # Цикл не позволяет бесконечно итерировать рекурсию при ошибке, благодаря этому не выйдет исключение RecursionError
    while True:
        try:
            print(f'МЕНЮ ВЗАИМОДЕЙСТВИЯ С ДАННЫМИ ПОЧТЫ\n'
                f'{'-' * 30}\n'
                f'1. Поиск данных по имени.\n'
                f'2. Добавить новые данные.\n'
                f'3. Изменить данные по имени.\n'
                f'4. Удалить данные по имени.\n'
                f'5. Выход\n')

            # Выбор варианта пользователем
            choice = int(input('Введите выбранный пункт: '))

            # Проверка на ввод допустимого значения от 1 до 5
            if choice < LOOK_UP or choice > QUIT:
                return choice
            else:
                print('Ошибка: введите число от 1 до 5.')   

        # Не дает коду упасть при вводе неверного значения, буквы/символа
        except ValueError:
            logging.error('Введен недопустимый символ (не число)')
            print('Ошибка: пожалуйста, введите цифру от 1 до 5.')


# Функция выполняет поиск даты по имени друга
def look_up(email):
    logging.debug(f'Функция look_up приняла словарь email_adress без ошибок.\n')
    # Ввод имени
    name = input('Введите имя: ')

    # Поиск по ключу(имени) через модуль get который 
    # возвращает по ключу значение(дату дня рождения) 
    # если имени нет в словаре то вернет не найдено
    print(email.get(name, 'Не найдено.'))


# Функция добавляет в словарь имя и дату
def add(email):
    logging.debug(f'Функция add приняла словарь email_adress без ошибок.\n')
    # Ввод имени и даты
    name = input('Введите имя: ')
    email_adress = input('Введите адрес электронной почты: ')

    # Проверка условием, если имени нету в словаре, то
    # добавляется новая пара ключ:значение где ключ - name, значение - email_adress
    # Если имя есть то выводит запись уже существует
    if name not in email:
        email[name] = email_adress
    else:
        print('Эта запись уже существует.')


# Функция позволяет именять дату рождения у уже добавленных имен
def change(email):
    logging.debug(f'Функция change приняла словарь email_adress без ошибок.\n')
    # Ввод имени для поиска
    name = input('Введите имя: ')

    # Проверка условием, если имя есть в словаре, то вводим новую дату рождения 
    # и обновляется пара ключ:значение где ключ - name, значение - bday
    # Если имени нету, то выводит Это имя не найдено.
    if name in email:
        email_adress = input('Введите новый адресс почты: ')

        email[name] = email_adress
    else:
        print('Это имя не найдено.')


# Функция удаляет друга из словаря
def delete(email):
    logging.debug(f'Функция delete приняла словарь email_adress без ошибок.\n')
    # Ввод имени для поиска
    name = input('Введите имя: ')

    # Проверка условием, если имя есть в словаре, то удаляем ключ и его значение с помощью del 
    # Если имени нету, то выводит Это имя не найдено.
    if name in email:
        del email[name]
    else:
        print('Это имя не найдено.')


# Функция расконсервирует и открывает файл
def open_data():
    logging.debug(f'Функция open_data приняла словарь email_adress без ошибок.\n')
    try:
        # Открытие файла для чтения двоичных файлов
        with open(DATA_FILE, 'rb') as input_file:
            # Загружаем весь словарь одним махом
            email_adress = pickle.load(input_file)
            logging.info('Данные успешно загружены из файла.')
            return email_adress

    except FileNotFoundError:
        # Если файла нет (первый запуск), просто возвращаем пустой словарь
        logging.error(f'Произошла ошибка чтения.\n Проверьте название файла: \n{DATA_FILE}')
        return {}        
        
    except EOFError:
        # Если файл пустой
        logging.info('Файл пуст. Создан новый пустой словарь.')
        return {}
    
    logging.debug(f'Функция open_data открыла файл без ошибок.')
    

# Функция сохраняет зашифрованный файл
def save_data(email):
    logging.debug(f'Функция save_data приняла словарь email_adress без ошибок.\n')
    try:
        # Открытие файла для консервации
        with open(DATA_FILE, 'wb') as output_file:
            pickle.dump(email, output_file)
    
    # Ловит ошибку неверного названия/пути файла
    except FileNotFoundError:
        logging.error(f'Произошла ошибка сохранения.\n Проверьте название файла: \n{DATA_FILE}')
        return None

    logging.debug(f'Функция save_data сохранила файл без ошибок.')


if __name__ == '__main__':
    main()