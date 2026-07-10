# Программа выводит только уникальные слова 

# Импортирую логгер 
import logging

# Путь к файлу
DATA_FILE = 'Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/Условия для задач/Шифруемый текст.txt'
# Шпаргалка по уровням доступа, отображает что ниже(если ERROR , то покажет: error и critical)
# logging.DEBUG      10 - Отладочная информация
# logging.INFO       20 - Обычная информация
# logging.WARNING    30 - Предупреждение
# logging.ERROR      40 - Ошибка
# logging.CRITICAL   50 - Критическая ошибка

# Базовая настройка логгера
logging.basicConfig(
    # Уровень доступа()
    level=logging.DEBUG,   
    # Формат отображения в файле/терминале      
    format= '%(asctime)s - %(levelname)s - %(message)s',
    # Путь к файлу
    #filename='Главы книги/Глава 9 - Словари и множества/Упражнения по программированию/№4 - Уникальные слова/app.log',
    # Способ записи
    #filemode='a'
)


# Основаня функция
def main():
    file = open_file()
    split_text = get_split_text(file)
    get_unique_words(split_text)


# Функция открывает и читает файл
def open_file():
    # Обработка ошибок с использование логгера вместо принта
    try:
        # Открываем для чтения
        with open(DATA_FILE, 'r', encoding='utf-8') as file:        
            line = file.readlines()
        
        logging.info(f'Результат открытия файла -> {line}\n')
        
        return line
    
    # Ловит ошибку неверного названия/пути файла
    except FileNotFoundError:
        logging.error(f'Произошла ошибка чтения.\n Проверьте название файла: \n{DATA_FILE}')
        return None
    
    # Ловит ошибку невозможности прочесть файл
    except IOError as e:
        logging.critical(f'Ошибка чтения файла {e}')
        return None


# Функция делает преобразование текста, т.к нужны лишь слова, то в функции происходит разделение -> слияение элементов
def get_split_text(file):
    logging.debug(f'Переменная успешно передана в функцию get_split_text\n')
    # Список принимающий текст
    text_list = []
    # По идее данный алгоритм имеет сложность O(n)
    for group in file:
        # Убираем в тексте \n и пробелы в начале и конце
        words = group.rstrip()
        # Объединяем в один список т.к words -> str тип данных
        text_list.append(words)

    # Объединяем в строку список
    merge_list = ' '.join(text_list)
    # Разделяем по ! -> получаем список
    split_exclamation_mark = merge_list.split('!')
    # Объединяем в строку
    merge_split_exclamation = ' '.join(split_exclamation_mark)
    # Разделяем по , -> получаем список
    split_comma = merge_split_exclamation.split(',')
    # Объединяем в строку
    merge_split_comma = ' '.join(split_comma)
    
    # Наглядная работа логгера, помогает увидеть преобразования каждой переменной
    # Отключается изменением на INFO в level
    logging.debug(f'text_list -> {text_list}')
    logging.debug(f'merge_list -> {merge_list}')
    logging.debug(f'split_exclamation_mark -> {split_exclamation_mark}')
    logging.debug(f'merge_split_exclamation -> {merge_split_exclamation}')
    logging.debug(f'merge_split_comma -> {merge_split_comma}\n')
    logging.info(f'Результат преоборазования текста: \n\t\t\t\t Было: -> {merge_list} \n\t\t\t\t Стало: -> {merge_split_comma}\n')
    return merge_split_comma


# Функция добавляет в множество и показывает уникальные слова
def get_unique_words(text):
    logging.debug(f'Переменная успешно передана в функцию get_unique_words\n')
    # Делим на список слов по пробелу
    words = [word for word in text.split(' ') if word]
    # Добавляем в множество
    unique_words = set(words)
    logging.info(f'Список уникальных слов: \n{unique_words}')


if __name__ == '__main__':
    main()
