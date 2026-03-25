# Программа удаляет запись с именем студента

import os

def main():
    # Флаг
    found = False

    # Поиск записи
    search = input('Какого студента желаете удалить? ')

    # Открыть исходный файл для чтения
    students_file = open('students.txt', 'r')

    # Открыть временный файл для записи
    temp_file = open('temp.txt', 'w')
    
    # Прочитать 1 строку с именем
    name = students_file.readline()

    # Цикл для прочетния файла
    while name != '':
        # Прочесть строку с баллами
        ball = int(students_file.readline())

        # Удалить \n
        name = name.rstrip('\n')

        # Условие if-else для проверки данных на удаление
        if name != search:
            # Поместить запись во временный файл
            temp_file.write(f'{name}\n')
            temp_file.write(f'{ball}\n')
        else:
            # Назначить флагу значение True
            found = True

        # Прочитать следующее значение
        name = students_file.readline()

    # Закрыть оба файла
    students_file.close()
    temp_file.close()

    # Удалить исходный файл
    os.remove('students.txt')

    # Переименовать временный файл
    os.rename('temp.txt', 'students.txt')

    # Если искомое значение не найдено, то в if 
    # передается foud = False, если найдено то found = True
    if found:
        print('Файл обновлен')
    else:
        print('Это значение в файле не найдено')

# Вызов глав функции
if __name__ == '__main__':
    main()