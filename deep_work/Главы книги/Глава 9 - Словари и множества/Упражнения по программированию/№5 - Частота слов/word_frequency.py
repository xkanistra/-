# Программа считае кол-во каждого слова в файле и добавляет их в словарь/файл

# Импорт логгера и re для удаления знаков препинания
import logging
import re

# Настройка логгера, простая
logging.basicConfig(
    level=logging.DEBUG,
    format= '%(asctime)s - %(levelname)s -> %(message)s',
    #filename='Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№5 - Частота слов/app.log',
    #filemode='a' 
)


OPEN_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/Шифруемый текст.txt'
SAVE_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№5 - Частота слов/Результат подсчета.txt'


# Основная функция
def main():
    file = open_file()
    text_list = get_text_list(file)
    words_dict = get_count_words(text_list)
    add_file(words_dict)


# Функция открывает файл для чтения
def open_file():
    # Ловим ошибки при выполнении
    try:
        # Открытие файла в формате чтения
        with open(OPEN_FILE, 'r', encoding='utf-8') as file:
            # Читаем файл чтобы он стал списком
            read_file = file.readlines()

        logging.info(f'Результат открытия файла -> {read_file}\n')
        return read_file

    # Ловит ошибку неверного названия/пути файла
    except FileNotFoundError:
        logging.error(f'Произошла ошибка чтения.\n Проверьте название файла: \n{OPEN_FILE}')
        return None
    
    # Ловит ошибку невозможности прочесть файл
    except IOError as e:
        logging.critical(f'Ошибка чтения файла {e}')
        return None


# Функция преобразует текст для последующего подсчета
# благодаря модулю re удалось сократить кол-во строк по сравнению с 4 задачей
def get_text_list(file):
    logging.debug(f'Переменная успешно передана в функцию get_text_list\n')
    text_list = []
    # Циклом удаляем \n, можно было бы удалить и все знаки препинания, 
    # но тогда пришлось бы их вручную вписывать, а это долго. В конце цикл добавляет в список слова без \n
    for item in file:
        words = item.strip()
        text_list.append(words)
    
    # Преобразуем список в строку и перевожу к нижнему регистру чтобы верно подсчитать слова не смотря на регис
    text = ' '.join(text_list).lower()
    # Модулем удаляем знаки препинания
    new_text = re.sub(r'[^\w\s]', '', text)
    # Разделяем текст по пробелу обратно в список
    split_text = new_text.split(' ')

    # Блок с откладкой, пишет шаги в консоли/файле
    logging.debug(f'Шаги работы алгорима преобразования текста:')
    logging.debug(f'file -> {text_list}')
    logging.debug(f'text_list -> {text}')
    logging.debug(f'text -> {new_text}')
    logging.debug(f'new_text -> {split_text}\n')
    logging.info(f'Результат выполнения преобразования текста -> {split_text}\n')

    return split_text


# Функция ведет подсчет кол-ва слов
def get_count_words(text_list):
    words_dict = {}
    for words in text_list:
        if words in words_dict:
            words_dict[words] += 1 
        else:
            words_dict[words] = 1
        
    
    logging.info(f'Результат подсчета -> {words_dict}\n')
    return words_dict


# Функция записывает в файл результат подсчета
def add_file(words_dict):
    # Ловим возможные ошибки
    try:
        # Открываем файл для записи(можно поставить формат записи a(append), он будет добавлять новые строки, а не презаписывать файл)
        with open(SAVE_FILE, 'w', encoding='utf-8') as save_file:
            # Читаем словарь, сразу делим на ключ/значение при помощи метода items()
            for k, v in words_dict.items():
                # Простое условие для красивой записи склонения слова раз, можно и без этого
                if v > 1:
                    # Запись в файл
                    save_file.write(f'Слово {k}, повторяется {v} раза\n')
                else:
                    save_file.write(f'Слово {k}, повторяется {v} раз\n')

        logging.info(f'Успешно сохранено в файл!')
    # Ловит ошибку неверного названия/пути файла
    except FileNotFoundError:
        logging.error(f'Произошла ошибка записи.\n Проверьте название файла: \n{SAVE_FILE}')
        return None
    
    # Ловит ошибку невозможности прочесть файл
    except IOError as e:
        logging.critical(f'Ошибка записи файла {e}')
        return None
    

if __name__ == '__main__':
    main()