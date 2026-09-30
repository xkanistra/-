# Программа демонстрирует работу подкласса ProductionWorker
import employee
import logging

LOGGER_FILE = "Главы книги/Глава 11 - Наследование/Упражнения по программированию/№2 - Класс ShiftSupervisor/app.log"

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
        annual_salary = float(input("Введите годовой оклад: "))
        annual_bonus = float(input("Введите годовую премию: "))
        suprevisor = employee.ShiftSupervisor(name, id_num, annual_salary, annual_bonus)
        logging.debug(
            f"Создан объект подкласса ProductionWorker в переменной worker.\n"
            f"Переданы 4 переменных: {name, id_num, annual_salary, annual_bonus}"
        )

        logging.info("Вывод данных")
        print("=========================================")
        print(
            f"Сотрудник: {suprevisor.get_name()}\n"
            f"ID-номер: {suprevisor.get_id_num()}\n"
            f"Годовой оклад: {suprevisor.get_salary()}$\n"
            f"Годовая премия: {suprevisor.get_bonus()}$"
        )

    except ValueError:
        logging.error(
            "Пользователь нарушил вводимый тип данных, ввел str вместо int/float"
        )
        print("Вы нарушили вводимый тип данных.")


if __name__ == "__main__":
    main()
