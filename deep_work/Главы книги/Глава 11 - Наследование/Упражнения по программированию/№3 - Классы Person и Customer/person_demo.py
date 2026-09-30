# Программа демонстрирует работу подкласса ProductionWorker
import person
import logging

LOGGER_FILE = "Главы книги/Глава 11 - Наследование/Упражнения по программированию/№3 - Классы Person и Customer/app.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s -> %(message)s",
    filename=LOGGER_FILE,
    filemode="a",
)


def main():
    logging.info("Начало программы.")
    logging.info("Ввод данных о сотруднике.")
    try:
        name = input("Введите имя клиента: ")
        adress = input("Введите адресс клиента: ")
        mobile_num = input("Введите номер мобильного телефона клиента: ")
        client_num = input("Введите номер клиента: ")
        mailing = int(
            input(
                "Введите согласие клиента на рассылку: \n1 - Согласен.\n2 - Не согласен.\n"
            )
        )
        while mailing < 1 or mailing > 2:
            logging.error(
                f"Пользователь ввел неверные данные: {mailing}. Вместо 1 или 2"
            )
            mailing = int(input("Введите номер  (1 - Согласен, 2 - Не согласен): "))

        logging.debug("Происходит создание булевых значений")
        if mailing == 1:
            mailing = True
        else:
            mailing = False

        customer = person.Customer(name, adress, mobile_num, client_num, mailing)
        logging.debug(
            f"Создан объект подкласса ProductionWorker в переменной worker.\n"
            f"Переданы 4 переменных: {name, adress, mobile_num, client_num, mailing}"
        )

        logging.info("Вывод данных")
        print("=========================================")
        print(
            f"Имя клиента: {customer.get_name()}\n"
            f"Адрес клиента: {customer.get_adress()}\n"
            f"Мобильный телефон клиента: {customer.get_mob_num()}\n"
            f"Номер клиента: {customer.get_client_num()}\n"
            f"Согласие с рассылкой: {customer.get_mailing()}"
        )

    except ValueError:
        logging.error(
            "Пользователь нарушил вводимый тип данных, ввел str вместо int/float"
        )
        print("Вы нарушили вводимый тип данных.")


if __name__ == "__main__":
    main()
