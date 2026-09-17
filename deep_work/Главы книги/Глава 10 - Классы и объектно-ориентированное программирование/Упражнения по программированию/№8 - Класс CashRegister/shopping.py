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


def main():
    price = load_item()


def load_item():
    with open(LOAD_FILE, "r", encoding="utf-8") as load_file:
        for line in load_file:
            strip_line = line.rstrip('\n')
            split_line = strip_line.split(',')
            description, quantity, price = split_line
            r_item = retailitem.RetailItem(description, int(quantity), float(price))
            print(r_item)

        # return description, quantity, price


if __name__ == "__main__":
    main()
