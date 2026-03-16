# Программа показывает записи 
# из файла coffee.txt

def main():
    # Открыть файл
    coffee_file = open('coffee.txt', 'r')

    # Прочитать поле с описанием первой строки
    descr = coffee_file.readline()

    # Прочитать остаток файла
    while descr != '':
        # Прочитать поле с кол-вом
        qty = float(coffee_file.readline())

        # Удалить \n из описания
        descr = descr.rstrip('\n')

        # Показать записи
        print(f'Описание: {descr}')
        print(f'Количество: {qty}')

        # Прочитать след. описание
        descr = coffee_file.readline()

    coffee_file.close()

if __name__ == '__main__':
    main()