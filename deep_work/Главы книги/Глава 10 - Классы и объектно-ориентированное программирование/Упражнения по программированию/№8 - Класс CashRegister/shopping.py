# Программа имитирует покупку товаров в магазине


import retailitem
import cashregister
import logging

# Глобальная константа имени файла
LOGGER_FILE = "Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№8 - Класс CashRegister/app.log"
LOAD_FILE = "Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№8 - Класс CashRegister/retail_file.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -> %(message)s",
    filename=LOGGER_FILE,
    filemode="a",
)

logging.debug("Это отладочное сообщение")
logging.info("Информационное сообщение")
logging.warning("Предупреждение")
logging.error("Ошибка")
logging.critical("Критическая ошибка\n")


# Главная функция
def main():
    logging.info('Программа запущенна.\n')
    again = "д"

    logging.debug("Создание объекта класса CashRegister.\n")
    # Создать пустой объект класса CashRegister
    cash_reg = cashregister.CashRegister()

    
    logging.info("Вызов функции load_item().")
    # Открытие и считывание информации из файла
    # открываем до цикла, чтобы повторно не открывать файл
    r_obj = load_item()

    logging.debug('Происходит запуск цикла while...\n')
    # Обрабатывать варианты выбора пока 
    # пользователь не пожелает закончить
    while again.lower() == "д":
        logging.info('Вызов функции get_menu_choice()')
        # Получить выбранный пользователем пункт меню
        choice = get_menu_choice(r_obj)

        logging.debug('Происходит добавление объекта класса RetailItem в объект класса CashRegister...')
        cash_reg.purchase_item(r_obj[choice])
        
        again = input('Желаете добавить еще вещь в корзину? (д/н): ')

    logging.info('Вывод информации о чеке, сумме и очистка кассы...')
    cash_reg.show_items()
    print(f'К оплате: {cash_reg.get_total()}$')
    cash_reg.clear()


# Функция load_item() загружает информацию из файла
# и передает её в качестве списка объектов
def load_item():
    logging.info('Функция load_item() начинает считывание файла...')
    logging.debug('Создан пустой список для объектов.')
    r_obj = []
    with open(LOAD_FILE, "r", encoding="utf-8") as load_file:
        logging.debug('Происходит преображение файла в список объектов...')
        for line in load_file:
            strip_line = line.rstrip("\n")
            split_line = strip_line.split(",")
            description, quantity, price = split_line
            r_item = retailitem.RetailItem(description, int(quantity), float(price))
            r_obj.append(r_item)

        logging.info('Функция завершила работу, возврат к выбору действия в меню.\n')
        return r_obj

# Функция get_menu_choice() выводит меню и получает
# проверенный на допустимость выбранный пункт
def get_menu_choice(r_obj):
    logging.info("Функция get_menu_choice() запущенна.")
    logging.debug("Происходит вывод меню.")
    print()
    print("Каталог")
    print("------------------------------------------")
    for index in range(len(r_obj)):
        print(f'{index + 1}. {r_obj[index].get_description()} - {r_obj[index].get_price()}$')
    
    logging.debug("Пользователь выбирает пункты меню.")
    # Получить выбранный пользователем пункт
    choice = int(input(f"Введите номер товара который хотите купить (1 - {len(r_obj)}): "))

    logging.warning("Происходит валидация данных введенных пользователем")
    # Проверка выбранного пункта на допустимость
    while choice < 1 or choice > len(r_obj):
        choice = int(input(f"Введите номер товар который хотите купить (1 - {len(r_obj)}): "))

    logging.info("Выбор пользователя отправлен в главную функцию.\n")
    # Вернуть выбранный пользователем пункт
    return choice - 1


if __name__ == "__main__":
    main()
