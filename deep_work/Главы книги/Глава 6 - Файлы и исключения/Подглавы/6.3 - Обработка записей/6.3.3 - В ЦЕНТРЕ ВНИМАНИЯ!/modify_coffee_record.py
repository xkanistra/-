# Программа позволяет изменять кол-во
# в записи файла coffee.txt

import os   # Модуль нужен для remane и remove

def main():
    # Создать булеву переменную для использования ее в качестве флага
    found = False

    # Получить искомое значение
    search = input('Введите искомое описание: ')
    new_qty = int(input('Введите новое кол-во: '))
    # Открыть исходный файл
    coffee_file = open('coffee.txt', 'r')

    # Открыть временный файл temp.txt
    temp_file = open('temp.txt', 'w')

    # Прочитать поле с описанием первой записи
    descr = coffee_file.readline()

    # Прочитать остаток файла
    while descr != '':
        # Прочесть поле с кол-вом
        qty = float(coffee_file.readline())

        # Удалить \n
        descr = descr.rstrip('\n')

        # Записать во временный файл либо эту запись
        # либо новую запись, если эта запись
        # подлежит изменению
        if descr == search:
            # Записать во временный файл запись
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')

            # Назначить флагу True
            found = True
        else:
            # Записать исходную запись во временный файл
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        # Прочитать след описание
        descr = coffee_file.readline()

    # Закрыть файл с данными о кофе и временный файл
    coffee_file.close()
    temp_file.close()

    # Удалить исходный файл
    os.remove('coffee.txt')

    # Переименовать временный файл
    os.rename('temp.txt', 'coffee.txt')

    # Есл искомое значение в файле не найдно
    # то показать сообщение
    if found:
        print('Файл обновлен')
    else:
        print('Значение в файле не найдено')

if __name__ == '__main__':
    main()