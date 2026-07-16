# Программа читает файл, собирает название команд, годы их побед и кол-во побед, после чего выводит список по запросу пользователя


import logging
from pydoc import text


DATA_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/WorldSeriesWinners.txt'


# Настройка логгера, простая
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    #filename='Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№7 - Победители Мировой серии/app.log',
    #filemode='a' 
)


def main():
    file = open_file()
    if not file:
        return
    winners_file = file
    winners_list = get_text_list(winners_file)
    get_winners_dict(winners_list)


# Функция открывает файл для чтения
def open_file():
    # Ловим ошибки при выполнении
    try:
        # Открытие первого файла в формате чтения
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            # Читаем файл чтобы он стал списком
            winners_file = file.readlines()

        logging.info(f'Результат открытия первого файла -> {winners_file}\n')

        return winners_file

    # Ловит ошибку неверного названия/пути файла
    except FileNotFoundError:
        logging.error(f'Произошла ошибка чтения.\n Проверьте название файла: \n{DATA_FILE}')
        return None
    
    # Ловит ошибку невозможности прочесть файл
    except IOError as e:
        logging.critical(f'Ошибка чтения файла {e}')
        return None
    

# Функция преобразует текст для последующего подсчета
def get_text_list(winners_file):
    logging.debug(f'Переменные успешно передана в функцию get_text_list\n')
    text_list = []

    # Циклом удаляем \n. В конце цикл добавляет в список слова без \n
    for item in winners_file:
        words = item.strip()
        text_list.append(words)

    # Блок с откладкой, пишет шаги в консоли/файле
    logging.debug(f'Шаги работы алгорима преобразования текста:')
    logging.debug(f'winners_file -> {text_list}\n')

    logging.info(f'Результат выполнения преобразования текста -> {text_list}\n')

    return text_list


# Не закончил задачу, нет концентрации
def get_winners_dict(winners_list):
    pass






if __name__ == '__main__':
    main()