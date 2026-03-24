# Программа читает файл number_list.txt выводит его на экран и закрывает файл

def main():
    number_file = open('number_list.txt', 'r')

    line = number_file.readline()

    while line != '':
        amount = int(line)
        
        print(f'{amount}')

        line = number_file.readline()

    number_file.close()

if __name__ == '__main__':
    main()
    