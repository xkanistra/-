# Программа читает и показывает содержимое
# файла philosophers.txt
def main():
    # Открыть файл с именем philosophers.txt
    infile = open('Главы книги/Глава 6 - Файлы и исключения/Подглавы/6.1 - Введение в файловый ввод и вывод/philosophers.txt', 'r')

    # Прочитать содержимое файла
    file_contents = infile.read()

    # Закрыть файл
    infile.close()

    # Напечатать данные, считанные 
    # в ОЗУ
    print(file_contents)

if __name__ == '__main__':
    main()