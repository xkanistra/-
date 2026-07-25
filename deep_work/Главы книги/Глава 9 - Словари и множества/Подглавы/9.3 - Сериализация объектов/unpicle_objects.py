# Программа демонстрирует расконсервацию файла
DATA_FILE = 'Главы книги/Глава 9 - Словари и множества/Подглавы/9.3 - Сериализация объектов/Файлы для примеров/info.dat'
import pickle

def main():
    # Флаг для управления циклом и чтобы обозначить конец файла
    end_of_file = False
    # Открытие файла для чтения двоичных файлов
    with open(DATA_FILE, 'rb') as input_file:
        # Читать файл до конца
        while not end_of_file:
            try:
                # Расконсервировать след объект
                person = pickle.load(input_file)
                # Показать объект
                display_data(person)
            
            except EOFError:
                # Установить флаг для обозначения достижения конца файла
                end_of_file = True

# Функция показывает данные о человеке в словаре который передан аргументом
def display_data(person):
    print('Имя:', person['имя'])
    print('Возраст', person['возраст'])
    print('Масса', person['масса'])
    print()

if __name__ == '__main__':
    main()