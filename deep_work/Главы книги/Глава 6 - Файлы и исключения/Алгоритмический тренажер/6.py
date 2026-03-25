# Программа открывает файл number_list.txt но не стирает его содержимое

def main():
    number_file = open('number_list.txt', 'a')

    for i in range(101, 201):
        number_file.write(f'{i}\n')

    number_file.close()

    print('Данные сохранены в файл')

if __name__ == '__main__':
    main()