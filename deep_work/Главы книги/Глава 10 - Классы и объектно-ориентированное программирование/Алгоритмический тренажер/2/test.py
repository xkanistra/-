# Тестирование класса Book
import book

def main():
    hline = input('Введите название заголовка: ')
    name = input('Введите имя автора: ')
    publisher = input('Введите имя издателя: ')

    add_inf = book.Book(hline, name, publisher)

    print(add_inf)

if __name__ == '__main__':
    main()