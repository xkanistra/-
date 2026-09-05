# Программа управляет контактами
import contact
import pickle

# Глобальные константы для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Глобальная константа имени файла
FILENAME = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Подглавы/10.3 - Работа с экземплярами/В ЦЕНТРЕ ВНИМАНИЯ1/contacts.dat'

# Главная функция
def main():
    # Загрузить существующий словарь контактов
    # и присвоить его переменной 
    mycontacts = load_contacts()

    # Переменная для выбора пользователя
    choice = 0

    # Обрабатывать варианты выбора пока 
    # пользователь не пожелает закончить
    while choice != QUIT:
        # Получить выбранный пользователем пункт меню
        choice = get_menu_choice()

        # Обработать выбранный вариант действий
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # Сохранить словарь в файле
    save_contacts(mycontacts)

# Функция загружает в словарь данные из файла/создает пустой словарь
def load_contacts():
    try:
        # Открыть файл contacts.dat
        with open(FILENAME, 'rb') as input_file:
            contact_dct = pickle.load(input_file)
    except EOFError:
        # Не получилось открыть файл 
        # поэтому создаем пустой словарь
        contact_dct = {}

    # Вернуть словарь
    return contact_dct

# Функция get_menu_choice() выводит меню и получает
# проверенный на допустимость выбранный пункт
def get_menu_choice():
    print()
    print('Меню')
    print('------------------------------------------')
    print('1. Найти контактное лицо')
    print('2. Добавить новое контактное лицо')
    print('3. Изменить существующее контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()

    # Получить выбранный пользователем пункт
    choice = int(input('Введите выбранный пункт: '))

    # Проверка выбранного пункта на допустимость
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    # Вернуть выбранный пользователем пункт
    return choice

# Функция look_up() отыскивает элемент 
# в заданном словаре
def look_up(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')

    # Отыскать его в словаре
    print(mycontacts.get(name, 'Это имя не найдено.'))

# Функция add добавляет новую запись в
# указанный словарь
def add(mycontacts):
    # Получить контактную информацию
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')

    # Создать именованную запись с объектом Contact
    entry = contact.Contact(name, phone, email)

    # Если имя не существует в словаре, то
    # добавить его в качестве ключа с имым значением 
    # в виде объекта
    if name not in mycontacts:
        mycontacts[name] = entry
    else:
        print('Это имя уже существует.')

# Функция change() позволяет изменять существующую
# запись в указанном словаре
def change(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')

    if name in mycontacts:
        # Получить новый телефонный номер
        phone = input('Введите новый телефонный номер: ')

        # Получить новый электронный адрес
        email = input('Введите новый электронный адрес: ')

        # Создать именованную запись с объектом Contact
        entry = contact.Contact(name, phone, email)

        # Обновить запись
        mycontacts[name] = entry
        print('Информация обновлена.')
    else:
        print('Это имя не найдено.')

# Функция delete() позволяет удалять
# запись из указанного словаря
def delete(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')

    # Если имя найдено, то удалить запись
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена.')
    else:
        print('Это имя не найдено.')

# Функция save_contacts() консервирует указанный 
# объект и сохраняет его в файле контактов
def save_contacts(mycontacts):
    # Открыть файл для записи
    with open(FILENAME, 'wb') as output_file:

        # Законсервировать словарь и сохранить его
        pickle.dump(mycontacts, output_file)

# Вызвать главную функцию
if __name__ == '__main__':
    main()