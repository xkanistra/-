# Программа записывает циклом числа от 1 до 100 в файл

def main():
    number_file = open('number_list.txt', 'w')

    for i in range(1, 101):
        number_file.write(f'{i}\n')

    number_file.close()

    print('Данные сохранены в файл')

if __name__ == '__main__':
    main()