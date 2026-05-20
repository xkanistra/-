# Вызов метода split, используя символ /

from datetime import date


def main():
    # Создать строковое значение
    date_string = '26/11/2020'

    # Разбить дату
    date_list = date_string.split('/')

    # Показать все части даты
    print(f'День: {date_list[0]}')
    print(f'Месяц: {date_list[1]}')
    print(f'Год: {date_list[2]}')

if __name__ == '__main__':
    main()