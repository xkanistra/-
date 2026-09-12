# Программа создает объекты класса Employee

import employee
import logging

SAVE_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№4 - Класс Employee/inf_file.txt'
LOGGER_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№4 - Класс Employee/app.log'


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
        name, id_num, department, position = get_information()
        inf_obj = add_inforamtion(name, id_num, department, position)
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
        name = input('Введите имя: ')
        id_num = int(input('Введите идентификационный номер: '))
        department = input('Введите отдел: ')
        position = input('Введите Должность: ')
        logging.info('Успешный ввод данных.')
        return name, str(id_num), department, position
    except ValueError:
        logging.error('Пользователь совершил неверный формат ввода.')
        print('Введите корректный возраст в числах.')


# Функция создает объекты класса и возвращает их значения
def add_inforamtion(name, id_num, department, position):
    logging.info('Функция add_inforamtion() успешно запущенна.')
    inf_obj = employee.Employee(name, id_num, department, position)
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

    