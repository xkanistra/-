# Программа демонстрирует работу подкласса ProductionWorker
import employee
import logging

LOGGER_FILE = "Главы книги/Глава 11 - Наследование/Упражнения по программированию/№1 - Классы Employee и ProductionWorker/app.log"

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
        name = input("Введите имя сотрудника: ")
        id_num = input("Введите ID-номер сотрудника: ")
        shift_num = int(input("Введите номер смены (1 - дневная, 2 - ночная): "))
        while shift_num < 1 or shift_num > 2:
            logging.error(
                f"Пользователь ввел неверные данные: {shift_num}. Вместо 1 или 2"
            )
            shift_num = int(input("Введите номер смены (1 - дневная, 2 - ночная): "))

        h_rate = float(input("Введите почасовую ставку: "))
        worker = employee.ProductionWorker(name, id_num, shift_num, h_rate)
        logging.debug(
            f"Создан объект подкласса ProductionWorker в переменной worker.\n"
            f"Переданы 4 переменных: {name, id_num, shift_num, h_rate}"
        )
        logging.info("Вывод данных")
        print("=========================================")
        print(
            f"Сотрудник: {worker.get_name()}\n"
            f"ID-номер: {worker.get_id_num()}\n"
            f"Смена: {worker.get_shift_num()}\n"
            f"Почасовая ставка: {worker.get_h_rate()}$"
        )

    except ValueError:
        logging.error(
            "Пользователь нарушил вводимый тип данных, ввел str вместо int/float"
        )
        print("Вы нарушили вводимый тип данных.")


if __name__ == "__main__":
    main()
