# Программа читает файл my_name.txt выводит содержимое на экран и закрывает файл

def main():
    name_file = open('my_name.txt', 'r')

    file_contecst = name_file.read()

    name_file.close()

    print(file_contecst)

if __name__ == '__main__':
    main()