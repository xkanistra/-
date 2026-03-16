# Программа производит поиск
# в файле coffee.txt записей, которые соответствуют
# описанию.

def main():
    # Создать булеву переменную для использования ее в качестве флага
    found = False

    # Получить искомое значение
    search = input('Введите искомое описание: ')

    # Открыть файл
    coffee_file = open('coffee.txt', 'r')

    # Прочитать поле с описанием первой записи
    descr = coffee_file.readline()

    # Прочесть остаток файла
    while descr != '':
        # Прочитать поле с кол-вом
        qty = float(coffee_file.readline())

        # Удалить \n
        descr = descr.rstrip('\n')

        # Определить соответствует ли запись поисковому
        # значению
        if descr == search:
            # Показать запись
            print(f'Описание: {descr}')
            print(f'количество: {qty}')
            print()
            # Назначить флагу found значение True
            found = True

        # Прочитать след. описание
        descr = coffee_file.readline()

    coffee_file.close()
    
    # Если поисковое значение в файле не найдено
    # то показать сообщение
    if not found:
        print('Это значение в файле не найдено.')

if __name__ == '__main__':
    main()