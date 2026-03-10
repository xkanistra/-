# Программа построчно читает 
# содержимое файла philosophers.txt
def main():
    # Открыть файл с именем philosophers.txt
    infile = open('Главы книги/Глава 6 - Файлы и исключения/Подглавы/6.1 - Введение в файловый ввод и вывод/philosophers.txt', 'r')

    # Прочитать три строки файла
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()\
    
    # Закрыть файл
    infile.close()

    # Напечатать данные
    # из ОЗУ
    print(line1)
    print(line2)
    print(line3)

if __name__ == '__main__':
    main()