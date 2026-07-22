# Программа находит слова в тексте и составляет словарь в котором слово:[строки где слово есть]
# затем сохраняет их в файле


# Импорт логгера и re для удаления знаков препинания
# и defaultdict для создания словаря списков
import logging
import re
from collections import defaultdict

READ_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№10 - Словарный индекс/Kennedy.txt'
SAVE_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№10 - Словарный индекс/index.txt'


# Настройка логгера, простая
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename='Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№10 - Словарный индекс/app.log',
    filemode='a' 
)


def main():
        file = open_file()
        if not file:
            return
        line_list = get_text_list(file)
        result = get_index_dict(line_list)
        save_file(result)


# Функция открывает файл для чтения
def open_file():
    # Ловим ошибки при выполнении
    try:
        # Открытие первого файла в формате чтения
        with open(READ_FILE, 'r', encoding='utf-8') as file:
            # Читаем файл чтобы он стал списком
            read_file = file.readlines()

        logging.info(f'Результат открытия файла -> {read_file}\n')

        return read_file 
    
    # Ловит ошибку неверного названия/пути файла
    except FileNotFoundError:
        logging.error(f'Произошла ошибка чтения.\n Проверьте название файла: \n{READ_FILE}')
        return None
    
    # Ловит ошибку невозможности прочесть файл
    except IOError as e:
        logging.critical(f'Ошибка чтения файла {e}')
        return None
    

# Функция преобразует текст для последующего подсчета
# благодаря модулю re удалось сократить кол-во строк по сравнению с 4 задачей
def get_text_list(file):
    logging.debug(f'Переменная успешно передана в функцию get_text_list\n')
    line_list = []

    # Циклом удаляем \n, можно было бы удалить и все знаки препинания, 
    # но тогда пришлось бы их вручную вписывать, а это долго. В конце цикл добавляет в список слова без \n
    for item in file:
        words = item.strip()
        line_list.append(words)

    # Блок с откладкой, пишет шаги в консоли/файле
    logging.debug(f'Шаги работы алгорима преобразования текста:')
    logging.debug(f'file -> {line_list}\n')

    logging.info(f'Результат выполнения преобразования текста -> {line_list}\n')

    return line_list


def get_index_dict(line_list):
    logging.debug(f'Переменная успешно передана в функцию get_index_dict\n')
    # Создаем словарь в котором автоматически создаются списки, уменьшает объем кода
    index_dict = defaultdict(list)
    
    for num, line in enumerate(line_list, 1):
        # Приводим к нижнему регистру и выделяем слова (только буквы/цифры)
        # Уменьшает код, т.к не нужно отдельным блоком кода удалять знаки препинания, мы их просто игнорируем
        words = re.findall(r'\w+', line)

        # Создаем множество, чтобы не дублировать номер строки если слово в строке повторяется
        unique_words = set(words)

        # Через цикл и множество создаем словарь -> слово:[строки где слово есть]
        for word in unique_words:
            index_dict[word].append(num)

    logging.debug(f'Шаги работы алгорима:\n')
    logging.debug(f'line_list -> {words}\n')
    logging.debug(f'words -> {unique_words}\n')
    logging.debug(f'index_dict -> {dict(index_dict)}')

    logging.info(f'Результат выполнения -> {dict(index_dict)}\n')

    # Возвращаем с dict чтобы убрать 'артефакты' работы модуля из collections
    return dict(index_dict)


# Функция записывает в файл результат подсчета
def save_file(result):
    logging.debug(f'Переменная успешно передана в функцию save_file\n')
    # Ловим возможные ошибки
    try:
        # Открываем файл для записи(можно поставить формат записи a(append), он будет добавлять новые строки, а не презаписывать файл)
        with open(SAVE_FILE, 'w', encoding='utf-8') as save_file:
            # Сохранение в файл через цикл отсортированного списка
            for word, lines in sorted(result.items()):
                # Преобразуем список в строку, разделяя слова запятой
                save_file.write(f'{word} : {", ".join(map(str, lines))}\n')

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