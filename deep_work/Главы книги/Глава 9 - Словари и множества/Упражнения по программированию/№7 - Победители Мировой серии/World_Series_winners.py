# Программа читает файл, собирает название команд, годы их побед и кол-во побед, после чего выводит список по запросу пользователя


import logging


DATA_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/WorldSeriesWinners.txt'


# Настройка логгера, простая
logging.basicConfig(
    level=logging.ERROR,
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
    wins_dict, year_dict = get_dicts(winners_list)
    get_result(wins_dict, year_dict)


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

    # Удаляем \n через списковое включение, читабельнее цикла
    text_list = [item.strip() for item in winners_file]

    # Блок с откладкой, пишет шаги в консоли/файле
    logging.debug(f'Шаги работы алгорима преобразования текста:')
    logging.debug(f'winners_file -> {text_list}\n')

    logging.info(f'Результат выполнения преобразования текста -> {text_list}\n')

    return text_list


# Функция создает словари
def get_dicts(winners_list):
    logging.debug(f'Переменные успешно передана в функцию get_dicts\n')
    wins_dict = {}
    year_dict = {}

    # Цикл для создания словаря {название команды:кол-во побед}
    for team in winners_list:
        # Фильтр чтобы для лет где не было игры
        if 'Not Played' in team:
            continue
        
        if team in wins_dict:
            wins_dict[team] += 1
        else:
            wins_dict[team] = 1

    # Цикл для создания словаря {год:название команды}
    # enumerate используется для удобства подсчета лет
    for year, team in enumerate(winners_list, 1903):
        # Фильтр чтобы для лет где не было игры
        if 'Not Played' in team:
            # pass не дает создать лишний номер при подсчете
            pass
        else:
            year_dict[year] = team

    # Информация для отладки
    logging.debug(f'Шаги работы алгорима создания словарей:')
    logging.debug(f'winners_list -> {wins_dict}\n'
                  f'\t\t\t\t   winners_list -> {year_dict}\n')

    logging.info(f'Результат создания словарей -> {wins_dict}\n'
                 f'\t\t\t\t   {year_dict}')
    
    return wins_dict, year_dict


# Функция позволяет выбрать год игры и показать результаты:
def get_result(wins_dict, year_dict):
    # Цикл не дает бесконечно нагружать память ПК и дает упасть при 1000 не верных вводов с RecursionError
    while True:
        # Важно иметь тут исключение, т.к тут пользователь взаимодейстует с кодом
        try:
            year = int(input('Примечание: 1904 и 1994 игры не проводились!\n'
                            f'Введите год игры(Игры проводились с 1903 - 2009): '))
            team = year_dict[year]
            wins = wins_dict[team]
            word = 'раза' if wins > 1 else 'раз'
            print(f'Команда "{team}" победила в {year} году и с 1903 - 2009 победла {wins} {word}')    

            break

        # Если введут не верный ключ, то появится информация об этом и цикл функция вызовется заново не давая упасть коду
        except KeyError:
            logging.error(f'Введен не верный номер ключа - {year}\n'
                        f'Доступны ключи: {year_dict.keys()}\n'
                        f'{wins_dict.keys()}\n')
            print(f'Попробуйте ввести еще раз год(1903 - 2009):')
            get_result(wins_dict, year_dict)
        # Если введут символ не крашнется программа
        except ValueError:
            logging.error(f'Введен лишний символ\n')
            print(f'Попробуйте ввести еще раз год без символов(1903 - 2009):')
            get_result(wins_dict, year_dict)
        

if __name__ == '__main__':
    main()