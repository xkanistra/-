# Программа показывает объекты класса RetailItem

import retailitem
import logging


SAVE_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№5 - Класс RetailItem/inf_file.txt'
LOGGER_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№5 - Класс RetailItem/app.log'


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename=LOGGER_FILE,
    filemode='a' 
)


def main():
    logging.info('Программа запущенна.')
    again = 'д'
    objects = []

    logging.debug('Начало цикла while.')
    while again.lower() == 'д':
        description, quantity, price = get_information()
        inf_obj = add_inforamtion(description, quantity, price)
        objects.append(inf_obj)
        again = input('Желаете продолжить ввод? (д/н): ')

    logging.debug('Начало цикла for.')
    for obj in objects:
        print(obj)

    logging.info('Цикл упешно вывел данные объектов класса.')
    logging.info('Программа завершенна.')


# Функция для ввода данных
def get_information():
    logging.info('Функция get_information() успешно запущенна.')
    try:
        description = input('Введите описание: ')
        quantity = int(input('Введите количество на складе: '))
        price = float(input('Введите цена: '))
        logging.info('Успешный ввод данных.')
        return description, quantity, price
    except ValueError:
        logging.error('Пользователь совершил неверный формат ввода.')
        print('Введите корректный возраст в числах.')
    except TypeError:
        logging.error('Пользователь совершил неверный формат ввода(запятая вместо точки).')
        print('Введите цену используя "," а не точку.')


# Функция создает объекты класса и возвращает их значения
def add_inforamtion(description, quantity, price):
    logging.info('Функция add_inforamtion() успешно запущенна.')
    inf_obj = retailitem.RetailItem(description, quantity, price)
    logging.info('Данные успешно переданы в функцию save_inf().')
    save_inf(inf_obj.inf_list())
    return inf_obj


# Функция сохраняет данные введённые пользователем в файле
def save_inf(information):
    logging.info('Функция save_inf() успешно запущенна.')
    with open(SAVE_FILE, 'a', encoding='utf-8') as save_file:
        save_file.write(f'{information}\n')
        logging.info('Данные сохранены успешно\n')


if __name__ == '__main__':
    main()