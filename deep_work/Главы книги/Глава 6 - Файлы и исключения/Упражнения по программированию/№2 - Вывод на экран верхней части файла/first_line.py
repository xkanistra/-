# Программа запрашивает у пользователя имя файла и выводит первые 5 строк файла

def main():
    # Задаем кол-во строк для прочтения
    num_line = int(input("Какое кол-во строк вы хотите вывести? "))

    # Узнаем имя файла
    filename = input("Введите имя файла: ")

    # Открываем файл
    file = open(filename, "r")

    # Цикл читающий кол-во строк в файле
    for i in range(1, num_line + 1):
        name = file.readline()
        print(name.rstrip("\n"))

    file.close()

if __name__ == '__main__':
    main()