# Программа показывет содержимое файла

def main():
    # Имя файла
    filename = input('Введите имя файла: ')

    # Открыть файл
    infile = open(filename, 'r')

    # Прочитать содержимое
    contents = infile.read()

    # Показать содержимое
    print(contents)

    infile.close()

if __name__ == '__main__':
    main()