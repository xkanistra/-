def main():
    number_file = open('6.12.txt', 'w')

    for i in range(1, 11):
        number = int(input(f'Введите {i} число: '))
        number_file.write(f'{number}\n')

    number_file.close()
    print('Данные сохранены в файл 6.12.txt')

if __name__ == '__main__':
    main()