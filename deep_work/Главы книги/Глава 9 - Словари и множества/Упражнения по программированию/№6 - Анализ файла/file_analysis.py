# Программа читает 2 файла, и сравнивает их содержимое и выводит:
# Cписок всех уникальных слов в обоих файла
# Список слов входящих в оба файла
# Список слов входящих в первый файл, но не входящий во второй и наоборот
# Список слов входящих, либо в первый, либо во второй файл


# Импорт логгера и re для удаления знаков препинания
import logging
import re


FIRST_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/Шифруемый текст.txt'
SECOND_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/Второй файл.txt'


# Настройка логгера, простая
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename='Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№5 - Частота слов/app.log',
    filemode='a' 
)


def main():
        files = open_file()
        if not files:
            return
        first_file, second_file = files
        first_list, second_list = get_text_list(first_file, second_file)
        get_comparisons(first_list, second_list)



# Функция открывает файл для чтения
def open_file():
    # Ловим ошибки при выполнении
    try:
        # Открытие первого файла в формате чтения
        with open(FIRST_FILE, 'r', encoding='utf-8') as file:
            # Читаем файл чтобы он стал списком
            first_file = file.readlines()

        logging.info(f'Результат открытия первого файла -> {first_file}\n')

        # Открытие второго файла в формате чтения
        with open(SECOND_FILE, 'r', encoding='utf-8') as file:
            # Читаем файл чтобы он стал списком
            second_file = file.readlines()

        logging.info(f'Результат открытия второго файла -> {second_file}\n')

        return first_file, second_file

    # Ловит ошибку неверного названия/пути файла
    except FileNotFoundError:
        logging.error(f'Произошла ошибка чтения.\n Проверьте название файла: \n{FIRST_FILE}')
        return None
    
    # Ловит ошибку невозможности прочесть файл
    except IOError as e:
        logging.critical(f'Ошибка чтения файла {e}')
        return None


# Функция преобразует текст для последующего подсчета
# благодаря модулю re удалось сократить кол-во строк по сравнению с 4 задачей
def get_text_list(first_file, second_file):
    logging.debug(f'Переменные успешно передана в функцию get_text_list\n')
    first_text_list = []
    second_text_list = []
    # Циклом удаляем \n, можно было бы удалить и все знаки препинания, 
    # но тогда пришлось бы их вручную вписывать, а это долго. В конце цикл добавляет в список слова без \n
    for item in first_file:
        words = item.strip()
        first_text_list.append(words)
    
    for item in second_file:
        words = item.strip()
        second_text_list.append(words)

    # Преобразуем список в строку. Делаем два преобразования в одной строке, экономим на строках кода
    first_text, second_text = ' '.join(first_text_list).lower(), ' '.join(second_text_list).lower()
    # Модулем удаляем знаки препинания. Делаем в одной строке
    new_first_text, new_second_text = re.sub(r'[^\w\s]', '', first_text), re.sub(r'[^\w\s]', '', second_text)
    # Разделяем текст по пробелу обратно в список. Делаем в одной строке
    split_first_text, split_second_text = new_first_text.split(), new_second_text.split()

    # Блок с откладкой, пишет шаги в консоли/файле
    logging.debug(f'Шаги работы алгорима преобразования текста:')
    logging.debug(f'first_file -> {first_text_list}\n'
                  f'\t\t\t\t   second_file -> {second_text_list}')
    logging.debug(f'first_text_list -> {first_text}\n'
                  f'\t\t\t\t   second_text_list -> {second_text}')
    logging.debug(f'fist_text -> {new_first_text}\n'
                  f'\t\t\t\t   second_text -> {new_second_text}')
    logging.debug(f'new_first_text -> {split_first_text}\n'
                  f'\t\t\t\t   new_second_text -> {split_second_text}\n')
    
    logging.info(f'Результат выполнения преобразования текста -> {split_first_text}, {split_second_text}\n')

    return split_first_text, split_second_text


# Функция производит сравнения содержимого двух файлов
def get_comparisons(first_list, second_list):
    logging.debug(f'Переменные успешно передана в функцию get_comparisons\n')

    # Перевожу списки в множества
    first_set = set(first_list)
    second_set = set(second_list)
    logging.info(f'Список уникальных слов в обоих файлах:\nПервый файл: {list(first_set)}\nВторой файл: {list(second_set)}')

    # Красивое внесение в список по условиям
    # Пересечение (И)
    intersection = list(first_set & second_set)
    logging.info(f'Список слов входящих в оба файла: {intersection}')

    # Разность (ТОЛЬКО в первом)
    diff_first = list(first_set - second_set)
    logging.info(f'Список слов входящих в первый файл, но не входящих во второй: {diff_first}')

    # Разность (ТОЛЬКО во втором)
    diff_second = list(second_set - first_set)
    logging.info(f'Список слов входящих во второй файл, но не входящих вперый: {diff_second}')

    # Симметричная разность (ИЛИ, но не И)
    sym_diff = list(first_set ^ second_set)
    logging.info(f'Список слов входящих либо в первый, либо во второй файл, но не входящих в оба файла одновременно: {sym_diff}')


if __name__ == '__main__':
    main()