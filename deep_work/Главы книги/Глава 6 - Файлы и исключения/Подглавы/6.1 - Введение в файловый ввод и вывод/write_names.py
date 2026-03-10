# Программа получает от пользователя три имени
# и пишет их в файл

def main():
    # Получить 3 имени
    print('Введите имена трех друзей')
    name1 = input('Друг # 1: ')
    name2 = input('Друг # 2: ')
    name3 = input('Друг # 3: ')

    # Открыть файл с именем friends.txt
    myfile = open('friends.txt', 'w')           # Для исп нужно будет вписать путь полный к файлу

    # Запимать имена в файл
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    # Закрыть файл
    myfile.close()
    print('Имена друзей были записаны в friends.txt')

if __name__ == '__main__':
    main()

# Строки с записью имен можно легко переписать с использованием f-строк
# myfile.write(f'{name1} \n')
# myfile.write(f'{name2} \n')
# myfile.write(f'{name3} \n')