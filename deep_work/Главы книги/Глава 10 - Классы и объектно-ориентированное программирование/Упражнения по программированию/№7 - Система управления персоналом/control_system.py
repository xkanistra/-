# Программа сохраняет объекты в словаре и помогает управлять ими через меню


import employee
import logging
import pickle


# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


# Глобальная константа имени файла
FILENAME = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№7 - Система управления персоналом/personal.dat'
LOGGER_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№7 - Система управления персоналом/app.log'


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename=LOGGER_FILE,
    filemode='a' 
)

logging.debug("Это отладочное сообщение")
logging.info("Информационное сообщение")
logging.warning("Предупреждение")
logging.error("Ошибка")
logging.critical("Критическая ошибка\n")

# Главная функция
def main():
    logging.info('Программа запущенна.\n')
    # Загрузить существующий словарь информации
    # о персонале
    personal_inf = load_personal_inf()

    # Переменная для выбора пользователя
    choice = 0

    logging.debug('Происходит запуск цикла while...\n')
    # Обрабатывать варианты выбора пока 
    # пользователь не пожелает закончить
    while choice != QUIT:
        # Получить выбранный пользователем пункт меню
        choice = get_menu_choice()

        # Обработать выбранный вариант действий
        if choice == LOOK_UP:
            look_up(personal_inf)
        elif choice == ADD:
            add(personal_inf)
        elif choice == CHANGE:
            change(personal_inf)
        elif choice == DELETE:
            delete(personal_inf)

    # Сохранить словарь в файле
    save_contacts(personal_inf)


# Функция загружает в словарь данные из файла/создает пустой словарь
def load_personal_inf():
    logging.info('Функция load_personal_inf() начинает считывание файла...')
    try:
        logging.debug('Идет считывание файла')
        # Открыть файл personal.dat
        with open(FILENAME, 'rb') as input_file:
            personal_dct = pickle.load(input_file)
    except EOFError:
        logging.error('Ошибка/невозможность открыть файл, он отсутствует или поврежден')
        logging.debug('Создан пустой словарь...')
        # Не получилось открыть файл 
        # поэтому создаем пустой словарь
        personal_dct = {}

    logging.info('Данные успешно прочитаны и переданы.\n')
    # Вернуть словарь
    return personal_dct


# Функция get_menu_choice() выводит меню и получает
# проверенный на допустимость выбранный пункт
def get_menu_choice():
    logging.info('Функция get_menu_choice() запущенна.')
    logging.debug('Происходит вывод меню.')
    print()
    print('Меню')
    print('------------------------------------------')
    print('1. Найти сотрудника')
    print('2. Добавить нового сотрудника')
    print('3. Изменить имя, отдел, должность сотрудника')
    print('4. Удалить сотрудника')
    print('5. Выйти из программы')
    print()

    logging.debug('Пользователь выбирает пункты меню.')
    # Получить выбранный пользователем пункт
    choice = int(input('Введите выбранный пункт: '))

    logging.warning('Происходит валидация данных введенных пользователем')
    # Проверка выбранного пункта на допустимость
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    logging.info('Выбор пользователя отправлен в главную функцию.\n')
    # Вернуть выбранный пользователем пункт
    return choice


# Функция look_up() отыскивает элемент 
# в заданном словаре
def look_up(personal_inf):
    logging.info('Функция look_up() запущенна.')

    logging.debug('Пользователь вводит ID искомого сотрудника')
    # Получить искомое имя
    id_num = input('Введите идентификационный номер сотрудника: ')

    # Отыскать его в словаре
    print(personal_inf.get(id_num, 'Этот сотрудник не найден.'))

    logging.info('Функция завершила работу, возврат к выбору действия в меню.\n')


# Функция add добавляет новую запись в
# указанный словарь
def add(personal_inf):
    logging.info('Функция add() запущенна.')
    logging.debug('Пользователь заполняет данные о сотруднике.')
    # Получить информацию о сотруднике
    name = input('Введите имя: ')
    id_num = input('Введите идентификационный номер: ')
    department = input('Введите отдел: ')
    position = input('Введите занимаемую должность: ')

    logging.debug('Создание объекта класса Employee')
    # Создать именованную запись с объектом Contact
    entry = employee.Employee(name, id_num, department, position)

    logging.debug('Происходит создание нового объекта в словаре.')
    # Если id номера не существует в словаре, то
    # добавить его в качестве ключа с имым значением 
    # в виде объекта
    if name not in personal_inf:
        personal_inf[id_num] = entry
    else:
        logging.warning('Сотрудник уже существует в словаре.')
        print('Данный сотрудник уже существует.')

    logging.info('Функция завершила работу, возврат к выбору действия в меню.\n')


# Функция change() позволяет изменять существующую
# запись в указанном словаре
def change(personal_inf):
    logging.info('Функция change() запущенна.')
    logging.debug('Происходит ввод ID сотрудника которому нужно изменить информацию.')
    # Получить искомое id работника
    id_num = input('Введите идентификационный номер: ')

    logging.debug('Происходит изменение информации о сотруднике.')
    if id_num in personal_inf:
        # Получить новое имя сотрудника
        name = input('Введите новое имя: ')
        # Получить новый отдел сотрудника
        department = input('Введите новый отдел: ')

        # Получить новую должность сотруника
        position = input('Введите новую занимаемую должность: ')

        logging.debug('Создание нового объекта класса Employee')
        # Создать именованную запись с объектом Employee
        entry = employee.Employee(name, id_num, department, position)

        logging.debug('Проихсодит обновление записи о сотруднике в словаре.')
        # Обновить запись
        personal_inf[id_num] = entry
        print('Информация обновлена.')
    else:
        logging.warning('Сотрудника нету в словаре.')
        print('Информации о сотруднике не найдено.')

    logging.info('Функция завершила работу, возврат к выбору действия в меню.\n')


# Функция delete() позволяет удалять
# запись из указанного словаря
def delete(personal_inf):
    logging.info('Функция delete() запущенна.')
    logging.debug('Происходит ввод ID сотрудника которого нужно удалить из словаря.')
    # Получить искомое ID
    id_num = input('Введите идентификационный номер сотрудника: ')

    logging.debug('Происходит удаление сотрудника из словаря.')
    # Если имя найдено, то удалить запись
    if id_num in personal_inf:
        del personal_inf[id_num]
        print('Запись удалена.')
    else:
        logging.warning('Сотрудника нету в словаре.')
        print('Это имя не найдено.')

    logging.info('Функция завершила работу, возврат к выбору действия в меню.\n')


# Функция save_contacts() консервирует указанный 
# объект и сохраняет его в файле контактов
def save_contacts(personal_inf):
    logging.info('Функция save_contacts() запущенна.')
    logging.debug('Происходит консервация словаря с данными о сотрудниках в зашифрованном файле.')
    # Открыть файл для записи
    with open(FILENAME, 'wb') as output_file:

        # Законсервировать словарь и сохранить его
        pickle.dump(personal_inf, output_file)

    logging.info('Функция завершила работу, возврат к выбору действия в меню.\n')


# Вызвать главную функцию
if __name__ == '__main__':
    main()